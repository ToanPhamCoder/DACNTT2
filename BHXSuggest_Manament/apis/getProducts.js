$(document).ready(function() {
    function fetchData(page) {
        var url = 'http://127.0.0.1:8000/products/all?size=10&page=' + page;
        $.ajax({
            url: url,
            method: 'GET',
            dataType: 'json',
            success: function(response) {
                var dataDiv = $('#dataProducts');
                dataDiv.empty();
                
                var table = $('<table></table>');
                var thead = $('<thead></thead>');
                var headerRow = $('<tr></tr>');
                headerRow.append('<th class="img-col">Hình ảnh</th>');
                headerRow.append('<th class="name-col">Tên sản phẩm</th>');
                headerRow.append('<th class="sup-col">Đề xuất</th>');
                headerRow.append('<th class="url-col">Đường dẫn</th>');
                thead.append(headerRow);
                table.append(thead);
                
                var tbody = $('<tbody></tbody>');
                response.data.forEach(function(item) {
                    var row = $('<tr></tr>');
                    row.append('<td><img src="' + item.img + '" alt="' + item.name + '"></td>');
                    row.append('<td>' + item.name + '</td>');
                    row.append('<td>' + Number((item.sup * 100).toFixed(2)) + ' %</td>');
                    row.append('<td><a target="_blank" href="' + item.url + '">Xem chi tiết</a></td>');
                    tbody.append(row);
                });
                table.append(tbody);
                dataDiv.append(table);
            },
            error: function(xhr, status, error) {
                $('#dataProducts').html('Error: ' + error);
            }
        });
    }

    $('#page').on('change', function() {
        var page = $(this).val();
        fetchData(page);
    });

    fetchData(0);
});
