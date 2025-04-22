# Product Management Full-Stack Application

A full-stack application built with Next.js (frontend) and FastAPI (backend) featuring authentication and product management capabilities.

## Tech Stack
- **Frontend**: Next.js 14, TypeScript, NextAuth, Shadcn UI
- **Backend**: FastAPI, Python
- **Authentication**: JWT, NextAuth
- **Data Fetching**: Rackbeat API integration

## Architecture Overview

### Frontend Architecture
- Next.js App Router with TypeScript
- NextAuth for session management with JWT storage
- Shadcn UI components with React Table for data presentation
- Axios for API communication
- Zod for form validation

### Backend Architecture
- FastAPI for REST API endpoints
- JWT authentication with OAuth2 password bearer flow
- Rackbeat API integration for product data
- Pagination and filtering logic
- Python-dotenv for environment management

## Setup Instructions

### Prerequisites
- Node.js 18+
- Python 3.9+
- Docker (optional)

### Environment Variables

#### Frontend (.env.local)
```env
NEXTAUTH_SECRET=super-secret-key
NEXTAUTH_URL=http://localhost:3000
NEXT_PUBLIC_BACKEND_URL=http://localhost:8000
```

#### Backend (.env)
```env
SECRET_KEY=super-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
RACKBEAT_API_KEY=your_rackbeat_api_key
RACKBEAT_API_URL=https://app.rackbeat.com/api
```

### Project Setup

#### Clone
```
git clone https://github.com/AbdulQadir1998/Fast-Stack.git
```

#### Frontend Setup
```
cd frontend
npm install
npm run dev
```

#### Backend Setup
```
cd backend
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate  # Windows
pip install -r requirements.txt
uvicorn app.main:app --reload
```

#### Docker Building and Running
```
docker-compose up --build
```

### Testing

- Access frontend http://localhost:3000
- Access backend http://localhost:8000

### Deployment Notes

- Ensure production environment variables are properly set

- Implement proper CORS configuration for production

- Use HTTPS in production environments
