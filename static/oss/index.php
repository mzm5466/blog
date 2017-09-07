<?php
$url0=$_SERVER['HTTP_REFERER'];//��ȡǰһҳ������
$url1=explode(":",$url0);// ��":"�ָ��ַ�
$url2=explode("/",$url1[1]);//��"/"�ָ��ַ�
$url=$url2[2];//��ȡ����
if($url=='pythoner.55555,io'){}
elseif($url=='mzm'){}

elseif($url=='ikuupyun.duapp.com'){}
//else {header("location:http://ikuup.net");}
else  echo $url;
?>

<html>
<head>
<meta http-equiv=Content-Type content="text/html;charset=utf-8">
<style type="text/css">
  body {margin: 0;font-family: "arial","΢���ź�";}
  .box {width: 578px;height: 258px;border: 1px dashed #ddd;padding: 10px 10px 0 10px;}
  .upbox {width: 100%;margin-bottom: 10px;height: 32px;font-size: 0;}
  .upbox .text {line-height: 23px;height: 30px;width: 450px;padding: 5px;float: left;outline-color: #4899E0;border: 1px solid #ddd;box-shadow: 1px 1px 3px #e8e8e8;}
  .upbox .btn {cursor: pointer;height: 30px;width: 80px;float: right;background-color: #4899E0;font-size: 14px;color: #fff;border: none;box-shadow: 1px 1px 3px #333;text-shadow: 1px 1px 1px #1c2f69;-webkit-transition: all 0.2s linear;-moz-transition: all 0.2s linear;-khtml-transition: all 0.2s linear;} 
  .upbox .btn:hover {background-color: #4899ff;}
  .tt {margin-top: 10px;font-size: 15px;text-shadow: 1px 1px 1px #bbb;color: #333;}
  #imgg {height: 100px;border: 2px dashed #ccc;padding: 5px;border-radius: 10px;-webkit-transition: all 0.2s linear;-moz-transition: all 0.2s linear;-khtml-transition: all 0.2s linear;}
  #imgg:hover {border: 2px dashed #444;}
  #imgAct {background: #3db0e9;background-image: -webkit-linear-gradient(left,#3db,#3de,3df,#3d9,#3d1,#3b9,#3db,#3d0 100%);}
  #loading_div {background: #3db0e9;height: 5px;box-shadow: 0px 0px 4px #59beec;border: 1px solid #fff;background-image: -webkit-linear-gradient(left,#3db,#3de,3df,#3d9,#3d1,#3b9,#3db,#3d0 100%);}
  </style>
<script src="js/loading.js" type="text/javascript"></script>
<script> function oCopy(obj){obj.select();js=obj.createTextRange();js.execCommand("Copy")}</script>
</head>
<body onLoad="setTimeout('enblur()', 500)">
<div class="box">
<form action="index.php" method="post" enctype="multipart/form-data">
<div class="upbox">
<input type="text" class="text" id="f_file" onClick="t_file.click()">
<input type="button" value="ѡ���ļ�" class="btn" onClick="t_file.click()">
<input name="file" type="file" id="t_file" onchange="f_file.value=this.value" style="display:none"></div>
<div class="upbox">
<input type="submit" name="submit" value="�ϴ�" class="btn" onclick="Loading('', 'LoadingJS/', 20, 100)"/>
 
</form>



<?php

define('OSS_ACCESS_ID', 'SIU1hLQRDBaz4LsR');
define('OSS_ACCESS_KEY', 'ioscmO5f0sT7fjtFPXX6WHWWA97Gni');
require_once 'sdk.class.php';
$oss_sdk_service = new ALIOSS();
$bucket = 'ikuup-net';



$data1 = "" . date('Y') . "";
$data2 = "" . date('m') . "";
$data3 = "" . date('d') . "";
$data4 = "" . date('H',time()) . "";
$data5 = "" . date('i',time()) . "";
$data6 = "" . date('s',time()) . "";
$datazip = "$data1/$data2/$data3/$data4-$data5-$data6";
$dataname = "$datazip/".$_FILES["file"]["name"]."";




if ((($_FILES["file"]["type"] == "image/gif")
|| ($_FILES["file"]["type"] == "image/jpeg")
|| ($_FILES["file"]["type"] == "image/png")
|| ($_FILES["file"]["type"] == "image/x-png")
|| ($_FILES["file"]["type"] == "application/zip")
|| ($_FILES["file"]["type"] == "application/x-zip-compressed")
|| ($_FILES["file"]["type"] == "application/octet-stream")
|| ($_FILES["file"]["type"] == "image/pjpeg"))
&& ($_FILES["file"]["size"] < 20971520))
{
    if ($_FILES["file"]["error"] > 0)
    {
        echo "��������: " . $_FILES["file"]["error"] . "<br />";
    }
    else
    {
      

        $content = '';
        $length = 0;
        $fp = fopen($_FILES["file"]["tmp_name"],'r');
        if($fp)
        {
            $f = fstat($fp);
            $length = $f['size'];
            while(!feof($fp))
            {
                $content .= fgets($fp,8192);
            }
        }
        $upload_file_options = array('content' => $content, 'length' => $length);
        $upload_file_by_content = $oss_sdk_service->upload_file_by_content($bucket, $dataname, $upload_file_options);
        $img_url = "http://oss.aliyuncs.com/" . $bucket . "/" . $dataname;
      echo "<input type=text class=text value=$img_url onclick=oCopy(this)></div>";
      echo "<div id=loading_div ></div>";
   $zipsize0=($_FILES["file"]["size"] / 1024); 
   $zipsize1=($_FILES["file"]["size"] / 1024/1024); 
   $zipsize3=number_format($zipsize0,2,".","");
   $zipsize4=number_format($zipsize1,2,".","");
if ($zipsize0 < 400)
    {echo "<div class=tt >������С: " . $zipsize3 . " KB</div>";}
else{
  echo "<div class=tt >������С: " . $zipsize4 . " Mb</div>";}

if (($_FILES["file"]["type"] == "image/gif")
|| ($_FILES["file"]["type"] == "image/jpeg")
|| ($_FILES["file"]["type"] == "image/png")
|| ($_FILES["file"]["type"] == "image/x-png")
|| ($_FILES["file"]["type"] == "image/pjpeg"))
{echo "<div class=tt ><a href=$img_url target=_blank><img id=imgg src=$img_url height=100/></a></div>";}
else      
{echo "<div class=tt ><a href=$img_url target=_blank><img id=imgg src=http://img-up.oss-cn-hangzhou.aliyuncs.com/img/zip.png height=100/></a></div>";}
}}
else
{
    echo "<input type=text class=text value=�ϴ������������ӡ� id=yao_txt></div>";
    echo "<div id=loading_div ></div>";
}

?>
</div>
</body>
</html>