from django.test import TestCase
from .models import Profile,Project,Score
import datetime as dt

# Create your tests here.
class ProjectTestClass(TestCase):
    '''
    setup self instance of project
    '''
    def setUp(self):
        self.post = Project(project_name='Awards',project_url='https://www.awwwards.com/',location='kenya')
    
    ''' 
    test instance of project
    '''
    def test_instance(self):
        self.assertTrue(isinstance(self.post,Project))


    '''
    test save project
    '''

    def test_save_image(self):
        self.post.save_project()
        project = Project.objects.all()
        self.assertTrue(len(project)>0)

class profileTestCLass(TestCase):
    '''
    setup self instance of profile
    '''
    def setUp(self):
        self.prof = Profile(Bio='Live the moment')
    
    ''' 
    test instance of profile
    '''
    def test_instance(self):
        self.assertTrue(isinstance(self.prof,Profile))

    def test_save_profile(self):
        self.prof.save_profile()
        bio = Profile.objects.all()
        self.assertTrue(len(bio)>0)

class ScoreTestCase(TestCase):
    '''
    setup
    '''
    def setUp(self):
        self.score = Score(design='2',usability='4',content='8',average='4.56',project='2')
    '''
    test instance of score
    '''
    def test_instance(self):
        self.assertTrue(isinstance(self.score,Score))
        '''
        test for save instance of score
        '''
    def test_save_score(self):
        self.score.save_score()
        name = Score.objects.all()
        self.assertTrue(len(name)>0)