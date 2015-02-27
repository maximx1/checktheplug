// Search functionality page
$(document).ready(function() {
    var timer, delay = 100;
    $('#searchBox').bind('keydown blur change', function(e) {
        var _this = $(this);
        clearTimeout(timer);
        timer = setTimeout(queryData, delay );
    });
});

var queryData = function() {
    var searchParam = $("#searchBox").val();
    if(searchParam.match(/^\s*$/g)) {
        $("#searchResultsTable").html("");
    }
    else {
        $.ajax({
            type: "GET",
            url: "/api/app/search/" + searchParam,
            success: function(data, textStatus, jqXHR) {
                updateTable(data);
            }
        });
    }
}

var updateTable = function(data) {
    if(data.status == "ok") {
        var tdata = "";
        var apps = data.apps;
        for(i = 0; i < apps.length; i++) {
            tdata += "<tr>";
            tdata += "<td>" + apps[i].id + "</td>";
            tdata += "<td>" + apps[i].appshortkey + "</td>";
            tdata += "<td>" + apps[i].name + "</td>";
            tdata += "<td>" + apps[i].description + "</td>";
            tdata += "<td>" + apps[i].host + "</td>";
            tdata += "</tr>";
        }
        $("#searchResultsTable").html(tdata);
    }
    else {
        $("#searchResultsTable").html("<h3>No Search Results</h3>");
    }
}