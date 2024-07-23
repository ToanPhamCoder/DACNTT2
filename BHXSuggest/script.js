$(document).ready(function() {
    $('#searchBox').on('keyup', function() {
        var query = $(this).val();

        $.ajax({
            url: 'http://127.0.0.1:8000/products/search',
            method: 'GET',
            data: { name: query },
            dataType: 'json',
            success: function(response) {
                var dataDiv = $('#data');
                dataDiv.empty();

                if (response.data.length > 0) {
                    response.data.forEach(function(item) {
                        var itemDiv = $('<div class="item"></div>');
                        itemDiv.append('<h3>' + item.name + '</h3>');
                        itemDiv.append('<img src="' + item.img + '" alt="' + item.name + '">');
                        itemDiv.append('<p>Người dùng yêu thích: ' + (item.sup * 100) + ' %</p>');
                        itemDiv.append('<a target="_blank" href="' + item.url + '">Xem chi tiết</a>');
                        dataDiv.append(itemDiv);
                    });
                } else {
                    dataDiv.append('<p>No products found.</p>');
                }
            },
            error: function(xhr, status, error) {
                $('#data').html('Error: ' + error);
            }
        });
    });
});
