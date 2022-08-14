# EBS - Python Internship
 This repository represents the list of tasks of the Python EBS internship.


**Milestone 1 Tasks** 

## 1. Add in Blog model a boolean field **enabled** to make some posts published or unpublished. 

Step 1: I added field `enabled` in Blog Model.
![image](https://i.imgur.com/wsZTGN8.png)


Step 2: I added this field into database table.

![image](https://i.imgur.com/pPfzanN.png)


Result:  
![image](https://i.imgur.com/EjP13LA.png)


## 2. Open in Django Admin (access /admin website section) and add in Blog list the real blog name and status (enabled/disabled): 

Step 1: I used:  python manage.py createsuperuser  `with username`: Cadi and `password`: 1234

Step 2: I created one blog.
![image](https://i.imgur.com/Y1aDf6F.png)


Result: 
![image](https://i.imgur.com/okx9Zw1.png)
![image](https://i.imgur.com/WrqvPBO.png)


## 3. Make an endpoint for create a blog post (similar as register endpoint) that will add a new record in blog table. 

Step 1: In *views.py* i added this class: 
![image](


Step 2: In *urls.py* i added this path: 
![image](


Step 3: In *serializers.py* i modified this class: 
![image](


Result:  
![image](


## 4. Create a new model **Comments** with **text** and **blog** foreign key, here we will save comments for each blog post. 

Step 1: In *models.py* i added this class: 
![image](


Step 2: I created *blog\_comments table:* 
![image](


## 5. Add Comments for management in Django Admin. 

Step 1: In *admin.py* i added this line: 
![image](


Results:  
![image](






## 6. Create an endpoint that creates a comment to a blog post (**input: blog\_id, text**) 

**Step 1: In** *views.py* i added this class: 
![image](


Step 2: In *serializers.py* i added this class: 
![image](


Step 3: In *urls.py* i added this path:  
![image](


**Result:** 
![image](


## 7. In endpoint **/blog/blog/{id}/** return the Blog post object and list of comments. 

Step 1: In *views.py* i modified BlogItemView class in: 
![image](


Result: 
![image](

