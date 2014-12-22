(function(){
    var app = angular.module('students', []);

    app.directive("studentSpecs", function() {
        return {
            restrict:"A",
            templateUrl: "student-specs.html"
        };
    });
    app.directive("studentDescription", function() {
        return {
            restrict: 'E',
            templateUrl: "student-description.html"
        };
    });

    app.directive("studentTabs", function() {
            return {
                restrict: "E",
                templateUrl: "student-tabs.html",
                controller: function() {
                    this.tab = 1;

                    this.isSet = function(checkTab) {
                        return this.tab === checkTab;
                    };

                    this.setTab = function(activeTab) {
                        this.tab = activeTab;
                    };
                },
                controllerAs: "tab"
            };
        });
});
