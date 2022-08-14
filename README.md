# EBS - Python Internship
 This repository represents the list of tasks of the Python EBS internship.


**Milestone 1 Tasks** 

1. Add in Blog model a boolean field **enabled** to make some posts published or unpublished. 

Step 1: 

![](Aspose.Words.1221bec9-c08e-4ee3-a6d3-05f9fa2af075.001.png)

Step 2: 

![](Aspose.Words.1221bec9-c08e-4ee3-a6d3-05f9fa2af075.002.png)

Result:  

![](Aspose.Words.1221bec9-c08e-4ee3-a6d3-05f9fa2af075.003.jpeg)

2. Open in Django Admin (access /admin website section) and add in Blog list the real blog name and status (enabled/disabled): 

Step 1: 

I used:  python manage.py createsuperuser  with username: Cadi and 

password: 1234

Step 2: 

![](Aspose.Words.1221bec9-c08e-4ee3-a6d3-05f9fa2af075.004.jpeg)

Result: 

![](Aspose.Words.1221bec9-c08e-4ee3-a6d3-05f9fa2af075.005.png)

![](Aspose.Words.1221bec9-c08e-4ee3-a6d3-05f9fa2af075.006.jpeg)

3. Make an endpoint for create a blog post (similar as register endpoint) that will add a new record in blog table. 

Step 1: In *views.py* i added this class: 

![](Aspose.Words.1221bec9-c08e-4ee3-a6d3-05f9fa2af075.007.jpeg)

Step 2: In *urls.py* i added this path: 

![](Aspose.Words.1221bec9-c08e-4ee3-a6d3-05f9fa2af075.008.png)

Step 3: In *serializers.py* i modified this class: 

![](Aspose.Words.1221bec9-c08e-4ee3-a6d3-05f9fa2af075.009.png)

Result:  

![](Aspose.Words.1221bec9-c08e-4ee3-a6d3-05f9fa2af075.010.jpeg)

4. Create a new model **Comments** with **text** and **blog** foreign key, here we will save comments for each blog post. 

Step 1: In *models.py* i added this class: 

![](Aspose.Words.1221bec9-c08e-4ee3-a6d3-05f9fa2af075.011.png)

Step 2: I created *blog\_comments table:* 

![](Aspose.Words.1221bec9-c08e-4ee3-a6d3-05f9fa2af075.012.png)

5. Add Comments for management in Django Admin. 

Step 1: In *admin.py* i added this line: 

![](Aspose.Words.1221bec9-c08e-4ee3-a6d3-05f9fa2af075.013.png)

Results:  

![](Aspose.Words.1221bec9-c08e-4ee3-a6d3-05f9fa2af075.014.png)

![](Aspose.Words.1221bec9-c08e-4ee3-a6d3-05f9fa2af075.015.jpeg)

![](Aspose.Words.1221bec9-c08e-4ee3-a6d3-05f9fa2af075.016.png)

6. Create an endpoint that creates a comment to a blog post (**input: blog\_id, text**) 

**Step 1: In** *views.py* i added this class: 

![](Aspose.Words.1221bec9-c08e-4ee3-a6d3-05f9fa2af075.017.png)

Step 2: In *serializers.py* i added this class: 

![](Aspose.Words.1221bec9-c08e-4ee3-a6d3-05f9fa2af075.018.png)

Step 3: In *urls.py* i added this path:  

![](Aspose.Words.1221bec9-c08e-4ee3-a6d3-05f9fa2af075.019.png)

**Result:** 

![](Aspose.Words.1221bec9-c08e-4ee3-a6d3-05f9fa2af075.020.jpeg)

7. In endpoint **/blog/blog/{id}/** return the Blog post object and list of comments. 

Step 1: In *views.py* i modified BlogItemView class in: 

![](Aspose.Words.1221bec9-c08e-4ee3-a6d3-05f9fa2af075.021.jpeg)

Result: 

![](Aspose.Words.1221bec9-c08e-4ee3-a6d3-05f9fa2af075.022.jpeg)
