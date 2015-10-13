var app = angular.module('FeedApp', []);
var obj;
var url = "http://feeds.feedburner.com/TechCrunch";
app.controller('FeedCtrl', function($scope, $http) {
    $scope.url_value="";
    $scope.init_cate = "Select category";
    $scope.init_feed = "Select Feed";
    $scope.text_value ="Select Category from drop down";
    $scope.hide_toggle = true;
    $scope.hide_count = true;
    $scope.changevalue = function (val, url) {
        $scope.init_feed = val;
        $scope.url_value = url;
        $http.jsonp('http://ajax.googleapis.com/ajax/services/feed/load?v=1.0&num=50&callback=JSON_CALLBACK&q=' + encodeURIComponent(url)).success(function(response) {
            $scope.feed_list = response.responseData.feed.entries;
        });
        $scope.hide_count = false;
    }
    $scope.filter_cate = function (c) {
        var arr=[];
        for (x = 0 ; x < obj.length ; x++) {
            if (obj[x].category == c){
                arr.push(obj[x]);
            }
        }
        $scope.url_value="";
        $scope.init_feed = "Select Feed";
        $scope.hide_toggle = false;
        $scope.sel_list = arr;
    }
    $http.get("https://tecnotree-7.0x10.info/api/tecnotree?type=json&query=list_feed").success(function(response) {
        $scope.cate = response.feed;
        obj = response.feed;
    });
});
