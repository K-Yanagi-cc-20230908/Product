@extends('frame/frame_base')

@section('header')
    <div class="header_left">
        <div class="header_logo">
            <img src="{{asset('./img/yana_logo.JPG')}}" class="header_logo_img">
        </div>
    </div>
    <div class="header_center"></div>
    <div class="header_right">
        <ul class="header_menus">
            <li class="header_menu">
                <a href="#" class="link">商品ページ</a>
            </li>
            <li class="header_menu">
                <a href="#" class="link">ゲーム紹介</a>
            </li>
            <li class="header_menu">
                <a href="#" class="link">ログイン</a>
            </li>
        </ul>
    </div>
@endsection

@section('footer')
    <div class="footer_left">
        <div class="footer_logo">
            <a href="{{route('homepage')}}" class="footer_logo_link">
                <img src="{{asset('./img/yana_logo.JPG')}}" class="footer_logo_img">
            </a>
        </div>
    </div>
    <div class="footer_center"></div>
    <div class="footer_right">
        <ul class="footer_menus">
            <li class="footer_menu">戻る</li>
            <li class="footer_menu">ホームページに戻る</li>
        </ul>
    </div>
@endsection