describe('navigation tabs test', function() {
  it('should change tabs', function() {
    browser.get('https://www.facebook.com/');
    //browser.waitForAngular();
    browser.driver.sleep(5);

    browser.actions().click(element(by.css('.nav.nav-tabs li:nth-child(2)>a'))).perform();
     expect(element(by.css('#admin .container-fluid h3')).isDisplayed()).toBeTruthy();
  });
});