package main

import (
	"bytes"
	"encoding/json"
	"log"
	"net/http"
	"os"
	"time"

	"github.com/google/uuid"
	"github.com/grid-x/webhook/examples/go-hmac-verification/pkg/hmac"
)

type PingEvent struct {
	ID              string        `json:"id"`
	Time            time.Time     `json:"time"`
	DataContentType string        `json:"dataContentType,omitempty"`
	SpecVersion     string        `json:"specVersion"`
	Source          string        `json:"source"`
	CorrelationID   string        `json:"correlationID,omitempty"`
	Type            string        `json:"type"`
	Data            PingEventData `json:"data,omitempty"`
}

type PingEventData struct {
	Message string `json:"message"`
}

func main() {
	secretKey := os.Getenv("HMAC_SECRET_KEY")
	if secretKey == "" {
		log.Fatalf("environment variable HMAC_SECRET_KEY must be set")
	}

	event := PingEvent{
		ID:              uuid.New().String(),
		Time:            time.Now(),
		DataContentType: "application/json",
		SpecVersion:     "1.0.0",
		Source:          "/systems/" + uuid.New().String(),
		CorrelationID:   uuid.New().String(),
		Type:            "ping",
		Data: PingEventData{
			Message: "hello world",
		},
	}

	bodyBytes, err := json.Marshal(event)
	if err != nil {
		log.Fatal(err)
	}

	req, err := http.NewRequest(http.MethodPost, "http://localhost:8080/hooks/xenon", bytes.NewBuffer(bodyBytes))
	if err != nil {
		log.Fatal(err)
	}

	signer := hmac.NewSigner(secretKey)
	if err := signer.Sign(req); err != nil {
		log.Fatal(err)
	}

	client := &http.Client{}
	res, err := client.Do(req)
	if err != nil {
		log.Fatal(err)
	}

	log.Println(res.StatusCode)
}
