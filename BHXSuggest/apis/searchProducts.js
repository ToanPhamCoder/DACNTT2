$(document).ready(function() {
    $('#searchBox').on('keyup', function() {
        var query = $(this).val();
        $.ajax({
            url: 'http://127.0.0.1:8000/products/search',
            method: 'GET',
            data: { name: query },
            dataType: 'json',
            success: function(response) {
                var dataDiv = $('#searchProducts');
                dataDiv.empty();
                if (response.data.length > 0) {
                    response.data.forEach(function(item) {
                        var itemDiv = $('<div class="item" style="display: flex; align-items: center; margin-bottom: 20px;"></div>');
                        var imgDiv = $('<div style="flex: 1;"></div>');
                        imgDiv.append('<img src="' + item.img + '" alt="' + item.name + '" style="width: 100px; height: 100px;">');
                        var infoDiv = $('<div style="flex: 2; padding-left: 20px;"></div>');
                        infoDiv.append('<h3>' + item.name + '</h3>');
                        infoDiv.append('<p>Người dùng yêu thích: ' + item.sup * 100 + ' %</p>');
                        infoDiv.append('<a target="_blank" href="' + item.url + '">Xem chi tiết</a>');
                        itemDiv.append(imgDiv);
                        itemDiv.append(infoDiv);
                        dataDiv.append(itemDiv);
                    });
                } else {
                    dataDiv.append('<p>Không tìm thấy sản phẩm</p>');
                }
            },
            error: function(xhr, status, error) {
                $('#data').html('Error: ' + error);
            }
        });
    });
});


// $(document).ready(function() {
//     $.ajax({
//         url: 'http://127.0.0.1:8000/products/search',
//         method: 'GET',
//         dataType: 'json',
//         success: function(response) {
//             var dataDiv = $('#dataCategories');
//             dataDiv.empty();
//             var temp = $('<div><p>Danh mục được mua nhiều</p></div>');
//             dataDiv.append(temp);
//             response.data.forEach(function(item) {
//                 var itemDiv = $('<div class="item" style="display: flex; align-items: center; margin-bottom: 20px;"></div>');
//                 var imgDiv = $('<div style="flex: 1;"></div>');
//                 imgDiv.append('<img src="' + item.img + '" alt="' + item.name + '" style="width: 300px; height: 300px;">');
//                 var infoDiv = $('<div style="flex: 2; padding-left: 20px;"></div>');
//                 infoDiv.append('<h3>' + item.name + '</h3>');
//                 infoDiv.append('<p>Người dùng yêu thích: ' + item.sup * 100 + ' %</p>');
//                 infoDiv.append('<a target="_blank" href="' + item.url + '">Xem chi tiết</a>');
//                 itemDiv.append(imgDiv);
//                 itemDiv.append(infoDiv);
//                 dataDiv.append(itemDiv);
//             });
//         },
//         error: function(xhr, status, error) {
//             $('#dataCategories').html('Error: ' + error);
//         }
//     });
// });
