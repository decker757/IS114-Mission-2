# PRD: IS114-Mission-2

## Overview
A school web project for SMU IS114 (Information Systems and Management or similar networking course). A multi-page website presenting a smart home IoT device — its name, purpose, features, and benefits — with networking demonstration (local hosting accessible from peer machines) and a video walkthrough. Assessed on content quality, networking concepts, demo, video, and writeup.

## Goals
- Build a multi-page static website for a smart home device concept
- Host locally and demonstrate accessibility from peer machines (client-server model)
- Include high-quality images/video
- Write clear, concise product copy
- Produce a video walkthrough

## Non-Goals
- Actual IoT device hardware
- Backend/API integration
- Production deployment
- Real-time device control

## User Stories
- As a student, I want to present my smart home device concept as a professional website.
- As an instructor, I want to see client-server networking concepts demonstrated practically.

## Tech Stack
- **Language**: HTML, CSS, JavaScript
- **Hosting**: Local (Python `http.server` or similar) — accessible on LAN
- **Assets**: images, video

## Architecture
```
IS114-Mission-2/
├── index.html           # Home page
├── about.html           # About the device
├── products.html        # Product features
├── data.html            # Data/specs page
├── paynow.html          # Payment/pricing concept
├── Posture_Checker.html # Specific device: Posture Checker
├── Eye_Care_Monitor.html
├── P_Watch.html
├── Availability_Status_Indicator.html
├── requirements.txt     # Python server deps (if any)
├── assets/              # Images, icons
├── scripts/             # JS files
└── backups/             # Dev backups
```

## Features
- Multi-page website with navigation between device pages
- Product marketing copy and imagery
- Networking demo: hosted via Python `http.server` on LAN
- Peer access via IP address on same network

## Deployment / Run
```bash
# Local hosting (accessible to peers on same network)
python -m http.server 8080
# or
python -m http.server
```

## Constraints & Notes
- **Academic**: graded project for IS114 networking course
- **LAN only**: demonstrated locally, not publicly deployed
- **Smart home device**: appears to cover multiple device concepts (Posture Checker, Eye Care Monitor, P-Watch, Availability Status Indicator) — each may be a team member's sub-project
