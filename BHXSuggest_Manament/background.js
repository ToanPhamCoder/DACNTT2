chrome.runtime.onInstalled.addListener(() => {
    console.log('Extension installed');
  });
  

  chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === "reloadTabs") {
      chrome.tabs.query({}, (tabs) => {
        for (let i = 0; i < tabs.length; i++) {
          chrome.tabs.reload(tabs[i].id);
        }
      });
      sendResponse({status: "reloading"});
    }
  });
  