@extends('frame/frame_temp')

@section('title', 'YANAYANAホームページ')

@section('css')
<link rel="stylesheet" href="{{asset('css/homepage.css')}}">
@endsection

@section('main')
    <div class="introduction">
        <div class="introduction_title">
            <h1 class="title">YANAYANAへようこそ！</h1>
            <div class="abstruct">
                <p>
                    YANAYANAへようこそ！
                </p>
                <p>
                    YANAYANAは数学・物理学・プログラミング・芸術・音楽を無料で学ぶことができるサイトです。
                </p>
                <p>
                    本サイトでは、最低限の予備知識として通常の高校生が学ぶ程度の数学が分かる事を仮定していますが、
                    それ以上の事は仮定しておりません。
                </p>
                <p>
                    ですので、学問を学びたい方なら以上の予備知識を持つ方ならば、幼稚園児でも学歴がなくてもかまいません。
                </p>
                <p>
                    学習方法ですが特に指定はありません。自分が思うままに自分が読みたいと思う項目にアクセスして適当に
                    呼んでいけば大丈夫です。
                    一から読まなくて大丈夫です。
                </p>
                <p>
                    それでは、自由に読み進めていってください。
                </p>
            </div>
        </div>
    </div>
    <div class="menus">

    </div>
    <div class="questions_box">

    </div>
@endsection