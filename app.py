from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
# Enable CORS for all routes
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/ats-score', methods=['POST'])
def ats_score():
    try:
        files = request.files.getlist('files')
        data_str = request.form.get('data')
        if data_str:
            data = json.loads(data_str)
            jobDescription = data.get('jobDescription')
            # TODO: Implement ATS score processing logic here
            
            # Return a markdown formatted string as expected by the frontend
            return """
## Resume Analysis

### Match Score: 85%

### Key Findings
- Strong match with technical requirements
- Good alignment with required experience
- Could improve emphasis on leadership skills

### Recommendations
1. Add more details about team leadership experience
2. Highlight project management skills
3. Include specific metrics and achievements

### Keyword Analysis
✅ Matched Keywords:
- Python
- React
- Node.js
- API Development

❌ Missing Keywords:
- Team Leadership
- Agile Methodology
- Budget Management
"""
    except Exception as e:
        return str(e), 400

@app.route('/summarize', methods=['POST'])
def text_summarizer():
    try:
        files = request.files.getlist('files')
        data_str = request.form.get('data')
        if data_str:
            data = json.loads(data_str)
            text = data.get('text')
            url = data.get('url')
            wordLimit = data.get('wordLimit')
            # TODO: Implement text summarization logic here
            
            return """
### Summary

This is a sample summary of the provided content, keeping within the specified word limit. The summary includes key points and main ideas from the original text while maintaining clarity and coherence.

### Key Points
- Main idea 1
- Main idea 2
- Main idea 3

### Source Analysis
- Word count: Original (1000) → Summary (150)
- Reading time: 2 minutes
"""
    except Exception as e:
        return str(e), 400

@app.route('/career-guide', methods=['POST'])
def career_guide():
    try:
        data_str = request.form.get('data')
        if data_str:
            data = json.loads(data_str)
            interests = data.get('interests')
            # TODO: Implement career guide logic here
            
            return """
## Career Recommendations

### Recommended Career Paths
1. **Software Developer**
   - Aligns with your interest in problem-solving
   - Strong job market demand
   - Opportunities for remote work

2. **Data Scientist**
   - Matches your analytical interests
   - Growing field with diverse applications
   - Combines technology and research

### Skills to Develop
- Programming: Python, JavaScript
- Data Analysis
- Machine Learning basics

### Next Steps
1. Take online courses in recommended areas
2. Build portfolio projects
3. Join professional communities
"""
    except Exception as e:
        return str(e), 400

@app.route('/interview-questions', methods=['POST'])
def interview_questions():
    try:
        data_str = request.form.get('data')
        if data_str:
            data = json.loads(data_str)
            skills = data.get('skills')
            # TODO: Implement interview questions generation logic here
            
            return """
## Technical Interview Questions

### Core Concepts
1. What is the difference between let, const, and var in JavaScript?
2. Explain how React's virtual DOM works
3. Describe the event loop in Node.js

### Problem Solving
1. How would you implement a debounce function?
2. Explain your approach to optimizing a slow database query
3. How would you design a scalable API endpoint?

### System Design
1. How would you design a real-time chat application?
2. Explain your approach to handling high traffic loads
3. Describe your strategy for data caching

### Best Practices
1. What are your preferred testing methodologies?
2. How do you approach code reviews?
3. Describe your git workflow
"""
    except Exception as e:
        return str(e), 400

@app.route('/project-ideas', methods=['POST'])
def project_ideas():
    try:
        data_str = request.form.get('data')
        if data_str:
            data = json.loads(data_str)
            skills = data.get('skills')
            difficulty = data.get('difficulty')
            # TODO: Implement project ideas generation logic here
            
            return """
## Project Suggestions

### 1. Real-time Chat Application
- **Tech Stack**: React, Node.js, Socket.io
- **Features**: 
  - Real-time messaging
  - User authentication
  - Message history
- **Learning Value**: WebSocket, Real-time data, Authentication

### 2. Task Management System
- **Tech Stack**: React, Express, MongoDB
- **Features**:
  - CRUD operations
  - User roles
  - Task assignments
- **Learning Value**: Full-stack development, Database design

### 3. Weather Dashboard
- **Tech Stack**: React, Weather API
- **Features**:
  - Location-based weather
  - 5-day forecast
  - Weather alerts
- **Learning Value**: API integration, Data visualization
"""
    except Exception as e:
        return str(e), 400

@app.route('/roadmap', methods=['POST'])
def roadmap():
    try:
        data_str = request.form.get('data')
        if data_str:
            data = json.loads(data_str)
            skill = data.get('skill')
            # TODO: Implement roadmap generation logic here
            
            return """
## Learning Roadmap

### 1. Fundamentals (Month 1)
- Basic syntax and concepts
- Development environment setup
- Version control with Git

### 2. Core Concepts (Month 2)
- Advanced language features
- Common design patterns
- Testing methodologies

### 3. Frameworks & Tools (Month 3)
- Popular frameworks
- Development tools
- Best practices

### Resources
- Online courses: Coursera, Udemy
- Documentation: MDN, React Docs
- Practice: LeetCode, HackerRank
"""
    except Exception as e:
        return str(e), 400

@app.route('/ideas-to-project', methods=['POST'])
def ideas_to_project():
    try:
        data_str = request.form.get('data')
        if data_str:
            data = json.loads(data_str)
            idea = data.get('idea', {})
            scope = data.get('scope', {})
            # TODO: Implement ideas to project logic here
            
            return """
## Project Implementation Plan

### Phase 1: Setup & Foundation
- Project structure setup
- Basic architecture design
- Core dependencies installation

### Phase 2: Core Features
- User authentication
- Basic CRUD operations
- API endpoints

### Phase 3: Advanced Features
- Real-time updates
- Data visualization
- Performance optimization

### Timeline & Milestones
1. Week 1-2: Setup and planning
2. Week 3-4: Core feature development
3. Week 5-6: Testing and refinement

### Tech Stack Recommendations
- Frontend: React with TypeScript
- Backend: Node.js with Express
- Database: PostgreSQL
"""
    except Exception as e:
        return str(e), 400

if __name__ == '__main__':
    app.run(debug=True, port=7051)