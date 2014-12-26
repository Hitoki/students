(function() {
    var app = angular.module('students', ['ngCookies']).run( function run( $http, $cookies ){
        $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
        $http.defaults.headers.post["Content-Type"] = "application/x-www-form-urlencoded";

        $http.defaults.headers.common['X-CSRFToken'] = $cookies.csrftoken;
        $http.defaults.headers.common["Content-Type"] = "application/x-www-form-urlencoded";
    });

    app.controller('StudentsController', function ($scope, $http) {

        $scope.students = [];
        $scope.edit_student = {};
        $scope.delete_student = {};

        $http.get('/api/v1/students/').success(function (data) {
            $scope.students = data;
        });

        $scope.showAddStudentForm = function () {
            $scope.add_student = {
                first_name: null,
                second_name: null,
                last_name: null,
                birth_date: null,
                student_card: null,
                group: null
            };
            angular.element('#add-student').modal('show');
        };


        $scope.createStudent = function(){
            $scope.add_student.group = $scope.add_student.group.id;
            $http.post('/api/v1/students/', $.param($scope.add_student)).success(function(data){
                $scope.students.push(data);
            });
        };

        $scope.deleteStudent = function (index, id) {
            $http.delete('/api/v1/students/' + id).success(function () {
                 $scope.students.splice(index, 1);
                angular.element('#delete-student').modal('hide');
            });
        };

    });


    app.controller('GroupsController', function ($scope, $http) {

        $scope.students_groups = [];
        $scope.edit_group = {};
        $scope.delete_group = {};
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

        $scope.deleteGroup = function (index, id) {
            $http.delete('/api/v1/students_groups/'+id).success(function(){
                $scope.students_groups.splice(index, 1);
            });
        };

        $scope.showDeleteForm = function (student) {
            $scope.students_groups.students = student;
            angular.element('#delete-student').modal('show');
        };

        $scope.showAddForm = function (group){
            $scope.add_group = group;
            angular.element('#add-group').modal('show');
        };

        $scope.addGroup = function (){
            $http.put('/api/v1/students_groups/', $scope.students_groups).success(function () {
                    $scope.students_groups.push($scope.students_groups);
                angular.element('#add-group').modal('hide');
            });

        $scope.addStudentInGroupForm = function (group){
            $scope.students_groups = group;
            angular.element('#add-student-to-group').modal('show');
        };

//            var data = { 'group': $scope.add_group};
//
//            $http.put('/api/v1/students_groups/', $scope.add_group).success(function (data) {
//                console.log(data);
//            });


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

})();

