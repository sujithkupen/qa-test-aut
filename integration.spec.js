const { test, expect } = require('@playwright/test');
const axios = require('axios');
const { backendUrl, frontendUrl } = require('./config');
test('Test if frontend displays message from backend', async ({ page }) => {

    // Fetch the expected message from the backend
    let expectedMessage;
    try {
        const response = await axios.get(backendUrl);
        expectedMessage = response.data.message;   
    } catch (error) {
        console.error('Error fetching from backend:', error);
        throw new Error('Error at the backend');
    }

    // Navigate to the frontend and verify
    await page.goto(frontendUrl);

    const messageElement = page.locator('h1');
    
    //console.log(messageElement.innerText())
        
    await expect(messageElement).toHaveText(expectedMessage);

    // Teardown 
    await page.close();
});

