(function() {
    var app = angular.module('students', ['ngRoute', 'ngCookies']).run( function run( $http, $cookies ){
        $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
        $http.defaults.headers.post["Content-Type"] = "application/x-www-form-urlencoded";

        $http.defaults.headers.common['X-CSRFToken'] = $cookies.csrftoken;
        $http.defaults.headers.common["Content-Type"] = "application/x-www-form-urlencoded";
    });

    app.directive('onFinishRender', function ($timeout) {
        return {
            restrict: 'A',
            link: function (scope, element, attr) {
                if (scope.$last === true) {
                    $timeout(function () {
                        scope.$emit('ngRepeatFinished');
                    });
                }
            }
        }
    });

    app.controller('mainCtrl', function ($scope, $http) {

        $scope.students = [];
        $scope.edit_student = {};
        $scope.delete_student = {};

        $scope.showAddForm = function (group){
            $scope.add_group = {
                title: null,
                steward: {
                    first_name: null,
                    second_name: null,
                    last_name: null,
                    birth_date: null,
                    student_card: null,
                    group: null
                },
                students: null
            };
            angular.element('#add-group').modal('show');
        };

        $scope.showAddSinGForm = function (group){
            $scope.sin_groups = group;
            angular.element('#add-student-to-group').modal('show');
         };

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
                angular.element('#add-student').modal('hide')
            });
        };

        $scope.deleteStudent = function (index, id) {
            $http.delete('/api/v1/students/' + id).success(function () {
                $scope.students.splice(index, 1);
                angular.element('#delete-student').modal('hide');
            });
        };

    });


    app.controller('GroupsController', function ($scope, $routeParams, $http) {

        $scope.students_groups = [];
        $scope.edit_group = {};
        $scope.delete_group = {};
        $scope.add_group = {};
        $scope.sin_groups = {};


        $http.get('/api/v1/students_groups/').success(function (data) {
            $scope.students_groups = data;
        });

        $scope.$on('ngRepeatFinished', function(ngRepeatFinishedEvent) {
            if($routeParams.group) {
                $('#student-list-'+$routeParams.group).modal('show');
            }
        });

        $scope.addSinG = function(){
            $scope.add_student.group = $scope.sin_groups.id;
            $http.post('/api/v1/students/', $.param($scope.add_student)).success(function(data){
                $scope.students.push(data);
                $scope.sin_groups.students.push(data);
            });
        };

        $scope.addGroup = function (){
            $http.post('/api/v1/students_groups/', $.param($scope.add_group)).success(function (data) {
                $scope.students_groups.push(data);
                angular.element('#add-group').modal('hide');
            });
        };

        $scope.showEditForm = function (group) {
            $scope.edit_group = group;
            angular.element('#edit-group').modal('show');
        };

        $scope.saveGroup = function () {
            console.log($scope.edit_group);
            $http.put('/api/v1/students_groups/'+$scope.edit_group.id, $scope.edit_group).success(function () {
                angular.element('#edit-group').modal('hide');
            })
        };

        $scope.showDeleteForm = function (student) {
            $scope.students_groups.students = student;
            angular.element('#delete-student').modal('show');
        };

        $scope.deleteGroup = function (index, id) {
            $http.delete('/api/v1/students_groups/'+id).success(function(){
                $scope.students_groups.splice(index, 1);
            });
        };

    });

    app.config(['$routeProvider', function($routeProvider) {
        $routeProvider.
            when('/:group', {
                templateUrl: '/page/group-list/',
                controller: 'GroupsController'
            }).when('/students/:students.id', {
                templateUrl: 'templates/student-detail.html',
                controller: 'StudentDetailCtrl'
            }).when('/', {
                templateUrl: '/page/group-list/',
                controller: 'GroupsController'
            })
            .otherwise({
                redirectTo: '/'
            });
    }]);

    app.controller('groupDetailController', ['$scope', '$http', function ($scope, $http) {
//        $http.get('/api/v1/students/?format=json').success(function(data) {
//            $scope.students = data;
//        });
        console.log(123);
//        $('.student-list').first().modal('show');
    }]);

    app.controller('StudentDetailCtrl', ['$scope', '$routeParams', function(
        $scope, $routeParams, $http) {
        $http.get('/api/v1/students/' + $routeParams.students.id +'.json').success(function(data) {
            $scope.students = data;
        });
    }]);
})();


