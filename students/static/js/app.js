(function() {
    var app = angular.module('students', ['ngCookies']).run( function run( $http, $cookies ){
        $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
        $http.defaults.headers.post["Content-Type"] = "application/x-www-form-urlencoded";

        $http.defaults.headers.common['X-CSRFToken'] = $cookies.csrftoken;
        $http.defaults.headers.common["Content-Type"] = "application/x-www-form-urlencoded";
    });

    app.controller('StudentsController', ['$http', function ($http) {
        var student = this;
        student.students = [];

        $http.get('/api/v1/students/').success(function (data) {
            console.log(data);
            student.students = data;
        });
    }]);

    app.controller('GroupsController', function ($scope, $http) {

        $scope.students_groups = [];
        $scope.edit_group = {};
        $scope.add_group = {};

        $http.get('/api/v1/students_groups/').success(function (data) {
            console.log(data);
            $scope.students_groups = data;
        });

        $scope.showEditForm = function (group) {
            $scope.edit_group = group;
            angular.element('#edit-group').modal('show');
        };

        $scope.saveGroup = function () {
            $http.put('/api/v1/students_groups/'+$scope.edit_group.id, $scope.edit_group).success(function () {
                angular.element('#edit-group').modal('hide');
            })
        };



        $scope.updateGroup = function (group) {
            $scope.edit_group = angular.copy(group)
        };

        $scope.showAddForm = function (group){
            $scope.add_group = group;
            angular.element('#add-group').modal('show');
        };

        $scope.addGroup = function (group){
            $http.put('/api/v1/students_groups/'+$scope.add_group.id, $scope.add_group).success(function () {
                angular.element('#add-group').modal('close');
            })
        };

    });

    app.directive('customPopover', function () {
        return {
            restrict: 'A',
            template: '<span>{{label}}</span>',
            link: function (scope, el, attrs) {
                scope.label = attrs.popoverLabel;

                $(el).popover({
                    trigger: 'click',
                    html: true,
                    content: attrs.popoverHtml,
                    placement: attrs.popoverPlacement
                });
            }
        };
    });

    app.controller('addCtrl', function (){

    });

})();

