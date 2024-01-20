<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class YanaController extends Controller
{
    public function homepage()
    {
        return view('yana.homepage');
    }
}
