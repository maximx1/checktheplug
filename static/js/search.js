// Search functionality page
$(document).ready(function() {
    var timer, delay = 100;
    $('#searchBox').bind('keydown blur change', function(e) {
        var _this = $(this);
        clearTimeout(timer);
        timer = setTimeout(queryData, delay );
    });
    queryData();
});

var queryData = function() {
    var searchParam = $("#searchBox").val();
    if(searchParam.match(/^\s*$/g)) {
        $("#searchResultsTable").children("tbody").html("<tr><td colspan='5'>No Search Results</td></tr>");
    }
    else {
        $.ajax({
            type: "POST",
            url: "/api/app/search/",
            data: JSON.stringify({ searchTerm: searchParam }),
            contentType: "application/json",
            success: function(data, textStatus, jqXHR) {
                updateTable(data);
            }
        });
    }
}

var updateTable = function(data) {
    if(data.status == "ok") {
        $("#searchResultsTable").children("tbody").html(data.apps.map(mapAppToRow).join(""));
        console.log("Hit")
    }
}

var mapAppToRow = function(app) {
    var tdata = "<tr>";
    tdata += "<td>" + app.id + "</td>";
    tdata += "<td>" + app.appshortkey + "</td>";
    tdata += "<td>" + app.name + "</td>";
    tdata += "<td>" + app.description + "</td>";
    tdata += "<td>" + app.host + "</td>";
    tdata += "</tr>";
    return tdata;
}