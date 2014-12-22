(function() {
    var app = angular.module('students', []);

    app.controller('StudentsController', ['$http', function ($http) {
        var student = this;
        student.students = [];

        $http.get('/api/v1/students/').success(function (data) {
            console.log(data);
            student.students = data;
        });
    }]);

    app.controller('GroupsController', ['$http', function ($http) {
        var group = this;
        group.students_groups = [];

        $http.get('/api/v1/students_groups/').success(function (data) {
            console.log(data);
            group.students_groups = data;
        });
    }]);
})();