# setup.py
from distutils.core import setup
import py2exe
 
setup(
	console=['extractXmlFromXL.py'],
	options = {
				'py2exe': {
							'packages': ['requests', 'requests.auth', 'openpyxl', 'logging'],
						}
				
			}
	)
