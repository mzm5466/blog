var frequency = 50;
//����   
var step = 3;
//������ɫ
var loadingBgcolor = "#f0f0f0";
//���
var loadingWidth = 576;
 
/*
*����˵��:
*content����ʾ���ݣ�����Ϊ�գ�
*imageURL��������JS�ļ���·�����ü��ɣ�
*left����������ʾλ��left
*top����������ʾλ��top
*/
function Loading(content,  imageURL, left, top) 
{ 
 imageURL = imageURL + "Loading.jpg";
  
 LoadTable(content, imageURL, left, top);
 showimage.style.display="";
 window.setInterval("RefAct();", frequency); 
}  
 
function RefAct()
{  
 imgAct.width += step;
 if(imgAct.width > loadingWidth-4)
 {
  imgAct.width = 0;
 }
}
 
function LoadTable(content, imageURL, left, top)
{
 var strLoading;
 strLoading = ""; 
 strLoading += "<div id=\"showimage\" style=\"DISPLAY:none;Z-INDEX:100;LEFT:" + left+ "px; align=\"center\">";
  strLoading += "<TABLE id=\"Table1\" cellSpacing=\"0\" cellPadding=\"0\" width=\"" + loadingWidth + "\" border=\"0\" bgcolor=\"" + loadingBgcolor+ "\">";
 if(content != "")
 {  
   strLoading += "<tr>";
    strLoading += "<td align=\"center\">";
     strLoading += "<font size=\"4\" face=\"Courier New, Courier, mono\"><strong>" + content + "</strong></font>";
    strLoading += "</td>";
   strLoading += "</tr>";
   strLoading += "<TR>";
 }
    strLoading += "<TD class=\"Loading\" height=\"5\">";
     strLoading += "<IMG id=\"imgAct\" height=\"5\" alt=\"\" src=\"" + imageURL + "\" width=\"0\">";
    strLoading += "</TD>";
   strLoading += "</TR>";
  strLoading += "</TABLE>";
 strLoading += "</div>";
 
 document.getElementById("loading_div").innerHTML = strLoading;
} 