mod-wsgi
<br/>
<?php echo date( "Y/m/d (D) H:i:s", time() ) ?>
<br/>
<?php echo gmdate("Y/m/d (D) H:i:s", time() ) ?>
<br/>
<?php
$week = array("日", "月", "火", "水", "木", "金", "土");
echo date( "n月j日", time() ) . $week[date( "w", time() ) ] . "曜日";
if(date("G", time()) > 12) echo "午後"; else echo "午前";
echo date( "g時i分", time() );
?>
<br/>
<?php echo date( "F j, Y (l)", time() ) ?>
<br/>
<?php echo date( 'Y/m/d (D) H:i:s', filemtime('index.html') ) ?>
<br/>
<?php echo date( 'Y/m/d (D) H:i:s', filemtime('0201_gt.php') ) ?>
<br/>
