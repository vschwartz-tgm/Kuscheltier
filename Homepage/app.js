// app.js
angular.module('myApp', [
  'ngRoute'
]).config(function($routeProvider) {
  $routeProvider.when("/", {
    templateUrl: "index.html",
  }).when("/pillenwecker", {
    templateUrl: "pillenwecker.html",
  })when("/buechervorlesen", {
    templateUrl: "buechervorlesen.html",
  })when("/notfallsignal", {
    templateUrl: "notfallsignal.html",
  }).otherwise({
    redirectTo: "/"
  });
});