#!/bin/bash

clear && sudo docker compose down && sudo docker compose up -d --build && sudo docker compose logs -f
