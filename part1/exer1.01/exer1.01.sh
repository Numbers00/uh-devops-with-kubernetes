#!/bin/bash

while true; do
  # Generate a random UUID (Universal Unique Identifier)
  random_uuid=$(uuidgen)

  # Get the current timestamp in ISO 8601 format
  timestamp=$(date -u +"%Y-%m-%dT%H:%M:%S.%3NZ")

  # Output the timestamp and random UUID
  echo "$timestamp: $random_uuid"

  # Sleep for 5 seconds
  sleep 5
done
