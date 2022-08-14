# EBS - Python Internship
 This repository represents the list of tasks of the Python EBS internship.


**Milestone 1 Tasks** 

## 1. Add in Blog model a boolean field **enabled** to make some posts published or unpublished. 

Step 1: I added field `enabled` in Blog Model.
![image](https://i.imgur.com/wsZTGN8.png)

Step 2: I added this field into database table.
![image](https://i.imgur.com/pPfzanN.png)

**Result**:  

![image](https://i.imgur.com/EjP13LA.png)


## 2. Open in Django Admin (access /admin website section) and add in Blog list the real blog name and status (enabled/disabled): 

Step 1: I used:  python manage.py createsuperuser  with `username`: Cadi` and `password: 1234`

Step 2: I created one blog.
![image](https://i.imgur.com/Y1aDf6F.png)

**Result**: 

![image](https://i.imgur.com/okx9Zw1.png)
![image](https://i.imgur.com/WrqvPBO.png)


## 3. Make an endpoint for create a blog post (similar as register endpoint) that will add a new record in blog table. 

Step 1: In *views.py* i added this class: 
![image](https://i.imgur.com/S5900xr.png)

Step 2: In *urls.py* i added this path: 

![image](https://i.imgur.com/ip5myk0.png)

Step 3: In *serializers.py* i modified this class: 

![image](https://i.imgur.com/vvFAc3t.png)

**Result**:

![image](https://i.imgur.com/yvE9QBX.png)


## 4. Create a new model **Comments** with **text** and **blog** foreign key, here we will save comments for each blog post. 

Step 1: In *models.py* i added this class: 
![image](https://i.imgur.com/0p0Y5Gv.png)

Step 2: I created *blog\_comments table:* 
![image](https://i.imgur.com/jTMmhEo.png)


## 5. Add Comments for management in Django Admin. 

Step 1: In *admin.py* i added this line: 
![image](https://i.imgur.com/H2Vlsj7.png)

**Result**:

![image](https://i.imgur.com/XdQCwmr.png)


## 6. Create an endpoint that creates a comment to a blog post (**input: blog_id, text**) 

**Step 1: In** *views.py* i added this class: 
![image](https://i.imgur.com/3vkEBAa.png)


Step 2: In *serializers.py* i added this class: 
![image](https://i.imgur.com/dfmJapL.png)


Step 3: In *urls.py* i added this path:  
![image](https://i.imgur.com/jYaNMUT.png)


**Result**:

![image](https://i.imgur.com/N7jRvjB.png)


## 7. In endpoint **/blog/blog/{id}/** return the Blog post object and list of comments. 

Step 1: In *views.py* i modified BlogItemView class in: 
![image](https://i.imgur.com/IEjeaH9.png)

**Result**:

![image](https://i.imgur.com/MpqfYtz.png)


### Remarks
- First I did each task separately, only after I finished I remembered the actions for evidence.
- It is possible to have forgotten certain actions
- In total, the whole set of tasks took me between 4 and 5 hours, I spent the most time on the first 3, the others were already a little easier.
- To fully see that everything works, I used `Postman`, an API testing software.
