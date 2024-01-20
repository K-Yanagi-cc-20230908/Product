<!DOCTYPE HTML>
<html lang="ja">
    <head>
        <meta charset="utf-8">
        <title>@yield('title')</title>
        <link rel="stylesheet" href="{{asset('css/homepage.css')}}">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>
        @yield('css')
        @yield('js')
    </head>
    <body>
        <header id="header">@yield('header')</header>
        <div id="main">@yield('main')</div>
        <footer id="footer">@yield('footer')</footer>
    </body>
</html>