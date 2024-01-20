<?php

use Illuminate\Support\Facades\Route;
//ホームページ
Route::get('homepage', 'App\Http\Controllers\YanaController@homepage')->name('homepage');
?>