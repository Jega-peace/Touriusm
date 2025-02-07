import streamlit as st
from streamlit_option_menu import option_menu

# Custom Styling
st.markdown("""
    <style>
        .main-title {
            font-size: 32px; 
            font-weight: bold;
            color: #471fa3; 
            text-align: center; 
            margin-bottom: 25px;
        }
        .section-title {
            font-size: 30px; 
            font-weight: bold; 
            color: #2E86C1; 
            margin-top: 20px;
            border-bottom: 3px solid #2E86C1;
            padding-bottom: 5px;
        }
        .content {
            font-size: 18px; 
            color: #34495E;
            margin-bottom: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# App Title
st.markdown('<div class="main-title">Tourism Guided System</div>', unsafe_allow_html=True)

# Sidebar Menu
with st.sidebar:
    select = option_menu(
       menu_title="Tourism Guide System",
       options=['Abstract', 'Company Profile', 'System Analysis', 'System Design', 'Modules Description', 'Database Schema','Database Execution'  ],
       icons=['info-circle', 'building', 'bar-chart', 'server', 'list-task', 'database','play-circle'],  # Added 'database' icon
       menu_icon="globe",  
       default_index=0
    )

# Abstract Section
if select == "Abstract":
    st.markdown('<div class="section-title">Abstract</div>', unsafe_allow_html=True)
    st.write("""
    The Tourism Guide System is a web-based or mobile application designed to provide tourists with comprehensive information about destinations. 
    The system includes details about attractions, accommodations, dining, transportation, and local events. 
    It offers personalized recommendations based on user preferences and features booking and itinerary planning functionality.
    
    **Domain:** Travel and Tourism Technology  
    **Technology Stack:**  
    - Backend: Python (Django/Flask)  
    - Frontend: HTML, CSS, JavaScript  
    - Database: MySQL  
    - APIs: Google Maps API, Amadeus, Sky Scanner, Expedia  
    """)

# Company Profile Section
if select == "Company Profile":
    st.markdown("<div class='section-title'>Company Profile</div>", unsafe_allow_html=True)
    st.markdown("""
    **Vinsup Infotech Private Limited** is an IT solutions provider specializing in **software consulting, development, and digital transformation**.  
    With over **8 years of experience**, the company offers services in **web & mobile development, cloud solutions, AI automation, and digital marketing**.

    **Address:**  
    No.246, P.M. Tower, Theni Main Road, Kalavasal Signal,  
    Madurai, Tamil Nadu - 625016

    **Core Services:**  
    - Custom Software Development  
    - IT Consulting & Facility Management  
    - AI & Cloud-based Solutions  
    - Digital Marketing  
    """)
    st.markdown("""
    <div style="text-align: center; margin-top: 20px;">
        <a href="https://vinsupinfotech.com/" target="_blank" 
        style="font-size: 18px; color: #ffffff; background-color: #2E86C1; padding: 10px 20px; 
        border-radius: 8px; text-decoration: none; display: inline-block;">
            Visit Vinsup Infotech
        </a>
    </div>
    """, unsafe_allow_html=True)

# System Analysis Section
if select == "System Analysis":
    st.markdown('<div class="section-title">System Analysis</div>', unsafe_allow_html=True)
    st.markdown("**Problem Statement:**")
    st.write("""
    Tourists often struggle to find authentic, updated, and personalized travel information.  
    The system solves this by providing AI-driven personalized suggestions and real-time travel insights.
    """)

    st.markdown("**Key Objectives:**")
    st.write("""
    - Provide detailed travel destination information  
    - Enable personalized itinerary planning  
    - Offer navigation and route suggestions  
    - Facilitate seamless bookings for travel services  
    """)

# System Design Section
elif select == "System Design":
    st.markdown('<div class="section-title">System Design</div>', unsafe_allow_html=True)
    
    st.markdown("**ER Diagram Entities:**")
    st.write("""
    - Users: Stores user details, preferences, and history  
    - Destinations: Contains information about travel locations  
    - Bookings: Manages user reservations  
    - Reviews: Handles user ratings and comments  
    - Itineraries: Enables travel planning  
    """)

    st.image("sd.jpg", caption="ER Diagram", use_container_width=True)
    
    st.markdown("**Sequence Diagram:**")
    st.write("""
    - Destination Search: User inputs query → System retrieves destinations → Displays results  
    - Booking Process: User selects a service → System verifies availability → Confirms booking  
    """)
    
    st.image("sdd.png", caption="Sequence Diagram", use_container_width=True)

# Modules Description Section
if select == "Modules Description":
    st.markdown('<div class="section-title">Modules Description</div>', unsafe_allow_html=True)
    
    modules = {
        "User Management Module": "Manages user accounts, profiles, and authentication.",
        "Destination Information Module": "Provides detailed information about tourist destinations.",
        "Recommendation Engine Module": "Suggests personalized destinations based on user behavior.",
        "Booking Module": "Facilitates online bookings for accommodations, transport, and tours.",
        "Itinerary Planner Module": "Enables users to create and manage personalized travel itineraries.",
        "Map and Navigation Module": "Provides location-based services and navigation assistance.",
        "Admin Module": "Allows administrators to manage content and user activities.",
        "Feedback and Review Module": "Collects and displays user reviews and ratings.",
        "Search and Filter Module": "Enhances user experience through advanced search functionalities.",
        "Notification Module": "Notifies users about bookings, updates, and personalized offers."
    }
    
    for module, description in modules.items():
        st.markdown(f"**{module}**")
        st.write(description)

# Database Schema Section
if select == "Database Schema":
    st.markdown('<div class="section-title">Database Schema</div>', unsafe_allow_html=True)
    st.write("""
    **1. Users Table:**
    - Fields: UserID, Name, Email, Password, Preferences.
    
    **2. Destinations Table:**
    - Fields: DestinationID, Name, Location, Description, Category, Images.
    
    **3. Bookings Table:**
    - Fields: BookingID, UserID, DestinationID, Type, Date, Status.
    
    **4. Reviews Table:**
    - Fields: ReviewID, UserID, DestinationID, Rating, Comment.
    
    **5. Itineraries Table:**
    - Fields: ItineraryID, UserID, Name, Destinations, Dates.
    
    """)

    st.markdown("**Django Models:**")
    st.code("""
from django.db import models
from django.contrib.auth.models import User

class Location(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='location_images/', blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.name

class Review(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} for {self.location.name}"

class Itinerary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    locations = models.ManyToManyField(Location)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    """, language="python")
    
  # System Execution Section
if select == "Database Execution":
    st.markdown('<div class="section-title">Database Execution</div>', unsafe_allow_html=True)

    st.write("""
    This section outlines the step-by-step execution of the Tourism Guide System, including running the server, adding data, 
    viewing the database, and processing models. Each step is accompanied by relevant images.
    """)

    execution_steps = [
        {
            "title": "Step 1: Running the Server",
            "description": "To start the application, run the following command in the terminal:",
            "command": "python manage.py runserver",
            "image": "s1.png",
            "sub_steps": [
                "Open your terminal and navigate to the project directory.",
                "Run the command to start the server: `python manage.py runserver`.",
                "The application should be accessible at `http://127.0.0.1:8000/`."
            ]
        },
        {
            "title": "Step 2: Accessing the Admin Panel",
            "description": "Once the server is running, access the Django admin panel to manage the application's data.",
            "command": "http://127.0.0.1:8000/admin/",
            "image": "s2.png",
            "sub_steps": [
                "Navigate to `http://127.0.0.1:8000/admin/` in your browser.",
                "Log in with the superuser credentials you created during setup."
            ]
        },
        {
            "title": "Step 3: Adding Data to the Database",
            "description": "Use Django’s admin panel or shell to insert records into the database tables.",
            "command": "python manage.py shell",
            "image": "Admin.jpg",
            "sub_steps": [
                "You can add data using the Django admin panel for the following sections:"
            ],
            "sub_steps_nested": [
                {
                    "title": "Step 3.1: Adding Location Data",
                    "description": "To add location data to the database, follow the steps below.",
                    "command": "python manage.py shell",
                    "image": "s3-1.png",
                    "sub_steps": [
                        "In the Django admin panel, navigate to the `Locations` section.",
                        "Click `Add New` to insert a new location.",
                        "Alternatively, you can add the location using Django ORM commands in the shell."
                    ]
                },
                {
                    "title": "Step 3.2: Adding Itinerary Data",
                    "description": "To add itinerary data to the database, follow the steps below.",
                    "command": "python manage.py shell",
                    "image": "s3-2.png",
                    "sub_steps": [
                        "In the Django admin panel, go to the `Itineraries` section.",
                        "Click `Add New` to create a new itinerary.",
                        "You can also use the Django shell to create itineraries using ORM commands."
                    ]
                },
                {
                    "title": "Step 3.3: Adding Review Data",
                    "description": "To add review data to the database, follow the steps below.",
                    "command": "python manage.py shell",
                    "image": "s3-3.png",
                    "sub_steps": [
                        "Navigate to the `Reviews` section in the Django admin panel.",
                        "Click `Add New` to insert a new review for a location.",
                        "You can also add reviews using Django ORM in the shell."
                    ]
                }
            ]
        },
        {
            "title": "Step 4: Viewing Data in SQLite Database",
            "description": "Verify the data stored in the database using the SQLite viewer .",
            "command": "python manage.py dbshell",
            "sub_commands": "Run `SELECT * FROM table_name;` to view the stored records.",
            "image": "s4.png",
            "image": "s4-1.png",
            "sub_steps": [
                "To view the database, open the project folder on VS code and view the SQLite database file.",
                
            ]
        }
    ]

    for step in execution_steps:
        # Display the step title
        st.markdown(f"### {step['title']}")
        # Write the description of the step
        st.write(step["description"])
        # Display the main command in a code block
        st.code(step["command"], language="bash")
        
        # Display substeps in bullet points
        for sub_step in step["sub_steps"]:
            st.write(f"✅ {sub_step}")

        # Display the image for the step
        st.image(step["image"], caption=step["title"], use_container_width=True)

        # If there are nested sub-steps (for adding Location, Itinerary, and Review data)
        if "sub_steps_nested" in step:
            for nested_step in step["sub_steps_nested"]:
                st.markdown(f"#### {nested_step['title']}")
                st.write(nested_step["description"])
                st.code(nested_step["command"], language="bash")
                for sub_sub_step in nested_step["sub_steps"]:
                    st.write(f"✅ {sub_sub_step}")
                st.image(nested_step["image"], caption=nested_step["title"], use_container_width=True)
