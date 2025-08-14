package main

import (
	"bytes"
	"encoding/json"
	"log/slog"
	"net/http"
	"os"
	"time"

	"github.com/google/uuid"
	"github.com/grid-x/webhook/examples/go-hmac-verification/pkg/hmac"
)

type PingEvent struct {
	ID              uuid.UUID     `json:"id"`
	Time            time.Time     `json:"time"`
	DataContentType string        `json:"dataContentType,omitempty"`
	SpecVersion     string        `json:"specVersion"`
	Source          string        `json:"source"`
	CorrelationID   uuid.UUID     `json:"correlationID,omitempty"`
	Type            string        `json:"type"`
	Data            PingEventData `json:"data,omitempty"`
}

type PingEventData struct {
	Message string `json:"message"`
}

func main() {
	secretKey := os.Getenv("HMAC_SECRET_KEY")
	if secretKey == "" {
		slog.Error("environment variable HMAC_SECRET_KEY must be set")
		os.Exit(1)
	}

	event := PingEvent{
		ID:              uuid.New(),
		Time:            time.Now(),
		DataContentType: "application/json",
		SpecVersion:     "1.0.1",
		Source:          "/systems/" + uuid.New().String(),
		CorrelationID:   uuid.New(),
		Type:            "ping",
		Data: PingEventData{
			Message: "hello world",
		},
	}

	bodyBytes, err := json.Marshal(event)
	if err != nil {
		slog.Error("failed marshalling body to JSON", "error", err)
		os.Exit(1)
	}

	req, err := http.NewRequest(http.MethodPost, "http://localhost:8080/hooks/xenon", bytes.NewBuffer(bodyBytes))
	if err != nil {
		slog.Error("failed creating request", "error", err)
		os.Exit(1)
	}

	requestSigner := hmac.NewRequestSigner([]string{secretKey})
	if err := requestSigner.Sign(req); err != nil {
		slog.Error("failed signing request", "error", err)
		os.Exit(1)
	}

	client := &http.Client{}
	res, err := client.Do(req)
	if err != nil {
		slog.Error("failed sending request", "error", err)
		os.Exit(1)
	}

	slog.Info("received response", "status", res.StatusCode)
}
