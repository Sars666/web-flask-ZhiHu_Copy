function openDialog() {
        document.getElementById('ask').style.display = 'block';
        document.getElementById('ask_bg').style.display = 'block';
    }
    function closeDialog() {
        document.getElementById('ask').style.display = 'none';
        document.getElementById('ask_bg').style.display = 'none';
    }
    function controlLen() {
        var inputText = document.getElementById('ask_title').value;
        if (inputText.length > 3) {
            document.getElementById('ask').style.height = '275px';
            document.getElementById('ask_header').style.height = '53px';
            document.getElementById('ask_detail').style.display = 'block';
            document.getElementById('ask_topic').style.display = 'block';
        }
    }
    function addTopic() {
        document.getElementById('ask_topicInput').style.display = 'block';
        document.getElementById('ask_topic').style.display = 'none';
    }
    function hideTopicInput() {
        document.getElementById('ask_topicInput').style.display = 'none';
        document.getElementById('ask_topic').style.display = 'block';
    }
    function addCommas(nStr) {
        nStr += '';
        x = nStr.split('.');
        x1 = x[0];
        x2 = x.length > 1 ? '.' + x[1] : '';
        var rgx = /(\d+)(\d{3})/;
        while (rgx.test(x1)) {
            x1 = x1.replace(rgx, '$1' + ',' + '$2');
        }
        return x1 + x2;
    }
    function addAnswer() {
        document.getElementById('addAnswer').style.display = 'block';
        document.getElementById('answers').style.top = '400px';
        document.getElementById('relate').style.position = 'relative';
        document.getElementById('relate').style.top = '-165px';
    }
    function showEdit(var1) {
        var var2 = var1 +'_c';
        document.getElementById(var1).style.display = '-webkit-box';
        document.getElementById(var2).style.display = 'none';
    }
    function hideEdit(var1) {
        var var2 = var1 +'_c';
        document.getElementById(var1).style.display = 'none';
        document.getElementById(var2).style.display = 'inline';
    }
    function showEditBut(var1){
        document.getElementById(var1).style.display = 'inline'
    }
    function hideEditBut(var1){
        document.getElementById(var1).style.display = 'none'
    }
    function showSaveImg(){
        document.getElementById('headImg').style.display = 'inline'
    }
function hideSaveImg(){
            document.getElementById('headImg').style.display = 'none'

}
    document.getElementById('followNum').innerHTML = addCommas('213213');
    document.getElementById('viewNum').innerHTML = addCommas('24325909');

