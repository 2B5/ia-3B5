exports.config = {
  seleniumAddress: 'http://localhost:4444/wd/hub',
  specs: ['teamWidgetTest.js'],
  capabilities: {
	  'browserName': 'chrome',
	  /*'chromeOptions': {
	    'args': ['--disable-web-security']
	  }*/
  }
};