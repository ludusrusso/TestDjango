from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()
        self.browser.implicit_wayt(3)


    def test_can_browse_the_blog(self):
        # Ludus is looking for the brand new blog ludusblog
        # he opens Firefox and browses to the link
        self.browser.get('http://127.0.0.1:8000')

        # Ludus notice that the title of the page is LudusBlog
        self.assertIn('LudusBlog', self.browser.title)

        # Ludus notice that there is an interesting post called 'first post'
        inputbox = self.browser.find_element_by_id('id_title_post')
        self.assertEqual(inputbox.text, 'first post')

        self.fail('finish the test')

        # Ludus clicks on the post title, the page chages


        # and start reading, he notice

        # Ludus is satisfed and closes the blog.

if __name__ == '__main__':
    unittest.main(warnings='ignore')
