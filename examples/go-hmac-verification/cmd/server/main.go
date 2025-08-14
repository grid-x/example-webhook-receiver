package main

import (
	"io"
	"log/slog"
	"net/http"
	"os"

	"github.com/grid-x/webhook/examples/go-hmac-verification/pkg/hmac"
)

func main() {
	secretKey := os.Getenv("HMAC_SECRET_KEY")
	if secretKey == "" {
		slog.Error("environment variable HMAC_SECRET_KEY must be set")
		os.Exit(1)
	}

	requestVerifier := hmac.NewRequestVerifier(secretKey)

	http.HandleFunc("/hooks/xenon", requestVerifier.Middleware(handler))

	slog.Info("Listening on port 8080")
	if err := http.ListenAndServe(":8080", nil); err != nil {
		slog.Error("Failed to listen on port 8080", "error", err)
	}
}

func handler(w http.ResponseWriter, r *http.Request) {
	body, err := io.ReadAll(r.Body)
	if err != nil {
		slog.ErrorContext(r.Context(), "failed to read body", "error", err)
		http.Error(w, "Failed to read request body", http.StatusInternalServerError)
	}

	slog.InfoContext(r.Context(), "Received request", "body", body)

	w.WriteHeader(http.StatusNoContent)
}
