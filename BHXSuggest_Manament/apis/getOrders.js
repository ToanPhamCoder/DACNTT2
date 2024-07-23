$(document).ready(function() {
    function fetchData(page) {
        var url = 'http://127.0.0.1:8000/order/all?size=10&page=' + page;
        $.ajax({
            url: url,
            method: 'GET',
            dataType: 'json',
            success: function(response) {
                var dataDiv = $('#dataOrders');
                dataDiv.empty();
                var tableRoot = $('<table></table>');
                var theadRoot = $('<thead></thead>');
                var headerRowRoot = $('<tr></tr>');
                headerRowRoot.append('<th>Mã đơn hàng</th>');
                headerRowRoot.append('<th>Thông tin đơn hàng</th>');
                theadRoot.append(headerRowRoot);
                tableRoot.append(theadRoot)
                var tbodyRoot = $('<tbody></tbody>');
                response.data.forEach(function(item) {
                    var sInfo = "<table>"

                    var table = $('<table></table>');
                    var thead = $('<thead></thead>');
                    var headerRow = $('<tr></tr>');
                    thead.append(headerRow);
                    table.append(thead);
                    
                    var tbody = $('<tbody></tbody>');
                    item.items.forEach(function(item) {
                        var sTemp = '<tr>' + '<td class="img-col"><img src="' + item.img + '" alt="' + item.name + '"></td>' + '<td class="name-col">' + item.name + '</td>' + '<td class="quan-col">' + item.quan + '</td>'
                        sInfo += sTemp
                    });
                    sInfo += "</table>"
                    table.append(tbody);

                    var rowRoot = $('<tr></tr>')
                    rowRoot.append('<td style = {}>'+item.orderId+'</td>')
                    rowRoot.append(sInfo)
                    tbodyRoot.append(rowRoot)
                });
                
                tableRoot.append(tbodyRoot)
                dataDiv.append(tableRoot)
            },
            error: function(xhr, status, error) {
                $('#dataCategories').html('Error: ' + error);
            }
        });
    }
    $('#pageOrder').on('change', function() {
        var page = $(this).val();
        fetchData(page);
    });
    fetchData(0);
});
