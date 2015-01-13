(function() {
    var app = angular.module('students', ['ngRoute', 'ngCookies']).run( function run( $http, $cookies ){
        $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
        $http.defaults.headers.post["Content-Type"] = "application/x-www-form-urlencoded";

        $http.defaults.headers.common['X-CSRFToken'] = $cookies.csrftoken;
        $http.defaults.headers.common["Content-Type"] = "application/x-www-form-urlencoded";
    });

    app.controller('mainCtrl', function ($rootScope, $http) {
        $http.get('/api/v1/students_groups/').success(function (data) {
            $rootScope.groups = data;
        });
    });

    app.controller('GroupController', function ($scope, $routeParams, $http) {
        $http.get('/api/v1/students_groups/'+$routeParams.group_id).success(function (data) {
            $scope.group = data;
            angular.element('#group-detail').modal('show');

            angular.element('#group-detail').on('hidden.bs.modal', function () {
                window.location.hash = '#/';
            });
        });
    });

    app.controller('EditGroupController', function ($scope, $rootScope, $routeParams, $http) {

        function showEditPopup(groups) {
            $scope.group = null;

            for (var i=0; i<groups.length; i++) {
                if(groups[i].id == $routeParams.group_id) {
                    $scope.group = groups[i];
                    break;
                }
            }

            angular.element('#edit-group').modal('show');

            angular.element('#edit-group').on('hidden.bs.modal', function () {
                window.location.hash = '#/';
            });
        }

        $scope.saveEditGroup = function () {
            $http.put('/api/v1/students_groups/'+$routeParams.group_id, $scope.group).success (function () {
                angular.element('#edit-group').modal('hide');
            });
        };

        if ($rootScope.groups) {
            showEditPopup($rootScope.groups);
        } else {
            $http.get('/api/v1/students_groups/').success(function (data) {
                $rootScope.groups = data;
                showEditPopup($rootScope.groups);
            });
        }

    });

    app.controller('AddStudentInGroupCtrl', function ($scope, $rootScope, $routeParams, $http) {

        function showAddStudentInGroupPopup(groups) {
            $scope.group = null;

            for (var i = 0; i < groups.length; i++) {
                if (groups[i].id == $routeParams.group_id) {
                    $scope.group = groups[i];
                    break;
                }
            }

            $http.get('/api/v1/students/').success(function (data) {
               $rootScope.students = data;
            });

            angular.element('#add-student-in-group').modal('show');

            angular.element('#add-student-in-group').on('hidden.bs.modal', function () {
                window.location.hash = '#/';
            });
        }

        var default_student = {
            first_name: null,
            second_name: null,
            last_name: null,
            birth_date: null,
            student_card: null,
            group: null
        };

        $scope.student = angular.copy(default_student);

        $scope.addStudentInGroup = function () {
            $scope.student.group = $routeParams.group_id;
            $http.post('/api/v1/students/', $.param($scope.student)).success(function(data){
                $rootScope.students.push(data);
                $scope.group.students.push(data);
                $scope.student = default_student;
            });
        };

        if ($rootScope.groups) {
            showAddStudentInGroupPopup($rootScope.groups);
        } else {
            $http.get('/api/v1/students_groups/').success(function (data) {
                $rootScope.groups = data;

                showAddStudentInGroupPopup($rootScope.groups);
            });
        }

    });

    app.controller('AddGroupCtrl', function ($scope, $rootScope, $routeParams, $http) {

            angular.element('#add-group').modal('show');

            angular.element('#add-group').on('hidden.bs.modal', function () {
                window.location.hash = '#/';
            });

        $scope.addGroup = function (){
            $http.post('/api/v1/students_groups/', $.param($scope.group)).success(function (data) {
                $rootScope.groups.push(data);
                angular.element('#add-group').modal('hide');
            });
        };

    });

    app.controller('DeleteGroupCtrl', function ($scope, $rootScope, $routeParams, $http) {

        function showDeleteGroupPopup(groups) {
            $scope.group = null;

            for (var i=0; i<groups.length; i++) {
                if(groups[i].id == $routeParams.group_id) {
                    $scope.group = groups[i];
                    break;
                }
            }

            angular.element('#group-delete').modal('show');

            angular.element('#group-delete').on('hidden.bs.modal', function () {
                window.location.hash = '#/';
            });
        }

        $scope.deleteGroup = function (index){
            $http.delete('/api/v1/students_groups/'+$routeParams.group_id).success(function(){
                $rootScope.groups.splice(index, 1);
                angular.element('#group-delete').modal('hide')
            });
        };

        if ($rootScope.groups) {
            showDeleteGroupPopup($rootScope.groups);
        } else {
            $http.get('/api/v1/students_groups/').success(function (data) {
                $rootScope.groups = data;
                showDeleteGroupPopup($rootScope.groups);
            });
        }

    });

    app.controller('StudentController', function ($scope, $routeParams, $http) {
        $http.get('/api/v1/students/'+$routeParams.student_id).success(function (data) {
            $scope.student = data;
            angular.element('#student-detail').modal('show');

            angular.element('#student-detail').on('hidden.bs.modal', function () {
                window.location.hash = '#/';
            });
        });
    });

    app.controller('AddStudentCtrl', function ($scope, $rootScope, $routeParams, $http) {

        angular.element('#add-student').modal('show');

        angular.element('#add-student').on('hidden.bs.modal', function () {
            window.location.hash = '#/';
        });

        $scope.addStudent = function (){
            $scope.student.group = $scope.student.group.id;
            $http.post('/api/v1/students/', $.param($scope.student)).success(function (data) {
                angular.element('#add-student').modal('hide');
            });
        };
    });

    app.controller('DeleteStudentCtrl', function ($scope, $rootScope, $routeParams, $http) {

        function showDeleteStudentPopup(students) {
            $scope.student = null;

            for (var i=0; i<students.length; i++) {
                if(students[i].id == $routeParams.student_id) {
                    $scope.student = students[i];
                    break;
                }
            }

            angular.element('#student-delete').modal('show');

            angular.element('#student-delete').on('hidden.bs.modal', function () {
                window.location.hash = '#/';
            });
        }

        $scope.deleteStudent = function (index){
            $http.delete('/api/v1/students/'+$routeParams.student_id).success(function(){
                $rootScope.students.splice(index, 1);
                angular.element('#student-delete').modal('hide')
            });
        };

        if ($rootScope.students) {
            showDeleteStudentPopup($rootScope.students);
        } else {
            $http.get('/api/v1/students/').success(function (data) {
                $rootScope.students = data;
                showDeleteStudentPopup($rootScope.students);
            });
        }

    });

    app.config(['$routeProvider', function($routeProvider) {
        $routeProvider.when('/', {
                controller: 'mainCtrl'
            }).when('/:group_id', {
                templateUrl: '/page/group-detail/',
                controller: 'GroupController'
            }).when('/:group_id/edit/', {
                templateUrl: '/page/group-edit/',
                controller: 'EditGroupController'
            }).when('/group/add/', {
                templateUrl: '/page/add-group/',
                controller: 'AddGroupCtrl'
            }).when('/:group_id/delete/', {
                templateUrl: '/page/group-delete/',
                controller: 'DeleteGroupCtrl'
            }).when('/student/:student_id', {
                templateUrl: '/page/student-detail/',
                controller: 'StudentController'
            }).when('/student-profile/add', {
                templateUrl: '/page/add-student/',
                controller: 'AddStudentCtrl'
            }).when('/student/:student_id/delete', {
                templateUrl: '/page/student-delete/',
                controller: 'DeleteStudentCtrl'
            }).when('/:group_id/add_student/', {
                templateUrl: '/page/add-student-in-group/',
                controller: 'AddStudentInGroupCtrl'
            });
//            .otherwise({
//                redirectTo: '/'
//            }).when('/:group', {
//                templateUrl: '/page/group-list/',
//                controller: 'GroupsController'
//            }).when('/students/:students.id', {
//                templateUrl: 'templates/student-detail.html',
//                controller: 'StudentDetailCtrl'
//            });
    }]);
})();


