chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
    var currentUrl = tabs[0].url;
    if (currentUrl.startsWith("https://www.bachhoaxanh.com")) {
        console.log("Đường dẫn hiện tại của tab:", currentUrl);
        $.ajax({
            url: "http://127.0.0.1:8000/products/related",
            type: "GET",
            data: {
                url: currentUrl
            },
            success: function(response) {
                if(response.status == 200){
                    var dataDiv = $('#suggestsCate');
                    dataDiv.empty();
                    var title = $('<div class="title"><h1>Thường được mua cùng với</h1></div>');
                    dataDiv.before(title);
                    response.data.forEach(function(item) {
                        var itemDiv = $('<div class="item"></div>');
                        var imgDiv = $('<div></div>');
                        imgDiv.append('<img src="' + item.img + '" alt="' + item.name + '">');
                        var infoDiv = $('<div class="info"></div>');
                        infoDiv.append('<h3>' + item.name + '</h3>');
                        infoDiv.append('<p>Đề xuất: ' + Number((item.sup * 100).toFixed(2)) + ' %</p>');
                        infoDiv.append('<a target="_blank" href="' + item.url + '">Xem chi tiết</a>');
                        itemDiv.append(imgDiv);
                        itemDiv.append(infoDiv);
                        dataDiv.append(itemDiv);
                    });
                }
                dataDiv.css({
                    'display': 'flex',
                    'overflow-x': 'auto',
                    'white-space': 'nowrap',
                    'width': '100%',
                    'max-width': '960px'
                });
                $('.item').css({
                    'flex': '0 0 200px',
                    'display': 'flex',
                    'flex-direction': 'column',
                    'align-items': 'center',
                    'margin-right': '20px',
                    'border': '1px solid #ccc',
                    'border-radius': '10px',
                    'padding': '10px',
                    'text-align': 'center'
                });
    
                $('.item img').css({
                    'width': '100px',
                    'height': '100px',
                    'border-radius': '10px'
                });
    
                $('.info').css({
                    'padding-left': '20px'
                });
            },
            error: function(xhr, status, error) {
                console.log("Error:", error);
            }
        });
    } 
});

