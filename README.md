### **Phase 1: Project Setup**
1. **Initialize a Django Project**  
   - ✅ Create a virtual environment  
   - ✅ Install Django and DRF  
   - ✅ Set up a new Django project and app

2. **Set Up Database (PostgreSQL/MySQL)**  
   - Configure `settings.py` to use PostgreSQL/MySQL  
   - Create necessary models (Users, Student Achievements)

---

### **Phase 2: Authentication System (JWT)**
3. **User Model & Role-Based Authentication**  
   - Extend Django’s `AbstractUser` to include a `role` field  
   - Implement JWT authentication using `djangorestframework-simplejwt`  
   - Create `/auth/login` API that verifies email, password, and role selection  

4. **Password Hashing** (Bonus)  
   - Use `bcrypt` or Django’s default hashing mechanism  

5. **Forgot Password Functionality** (Bonus)  
   - Implement email-based password reset  

---

### **Phase 3: Role-Based Access Control**
6. **Role-Based Dashboard Redirection**  
   - Return different responses based on user role after login  

7. **API Access Control**  
   - Use Django permissions to restrict:  
     - Schools (can manage student achievements)  
     - Parents & Students (can only view their own data)  

8. **Student Achievements API**  
   - Create `GET /student/achievements/{student_id}` endpoint  
   - Ensure proper role-based access control  

---

### **Phase 4: API Documentation & Testing**
9. **Postman Collection**  
   - Document all API endpoints and test them  

10. **Prepare README & Push Code to GitHub**  
   - Include setup instructions in `README.md`  

---