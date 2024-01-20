<?php
use Illuminate\Support\Facades\Route;
Route::get('zundamon/chat', 'App\Http\Controllers\ChatController@zundaChatForm')->name('zundaCahtForm');
?>