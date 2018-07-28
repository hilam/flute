import sys
sys.path.append('..')

import os
import unittest
from files.util import current_dir, create_app, delete_app

class TestApp( unittest.TestCase ):
    
    def test_initialize( self ):
        create_app()
        self.assertTrue( os.path.isdir( current_dir + '/app' ) )
        self.assertTrue( os.path.isdir( current_dir + '/config' ) )
        self.assertTrue( os.path.isfile( current_dir + '/settings.json' ) )
        self.assertTrue( os.path.isfile( current_dir + '/app.py' ) )
        delete_app()
        self.assertTrue( not os.path.isdir( current_dir + '/app' ) )
        self.assertTrue( not os.path.isdir( current_dir + '/config' ) )
        self.assertTrue( not os.path.isfile( current_dir + '/settings.json' ) )
        self.assertTrue( not os.path.isfile( current_dir + '/app.py' ) )

if __name__ == '__main__':
    unittest.main()