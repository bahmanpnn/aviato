function SendArticleComment(ArticleId){
    // console.log('SendArticleComment done!!')

    var comment=$('#text').val();
    var parentId=$('#parentId').val();

    console.log(comment);
    console.log(ArticleId);
    console.log(parentId);

    $.get('/blog/add-comment/article_comment/',{
        comment:comment,
        article_id:ArticleId,
        parent_id:parentId

    }).then(res=>{
        $('#comments_area').html(res)
        $('#commentText').val('');
        $('#parentId').val('');
        
        //after adding comment must scroll to that 
        if(parentId !== null && parentId !== ''){
            document.getElementById('single_comment_'+parentId).scrollIntoView({behavior:'smooth'})
        }else{
            document.getElementById('comments_area').scrollIntoView({behavior:'smooth'})
        }
    })
}

function fillParentId(parentId) {
    $('#parentId').val(parentId);
    document.getElementById('comment_form').scrollIntoView({behavior:'smooth'})
}














// function SendArticleComment(ArticleId){
//     // console.log('SendArticleComment done!!')

//     var comment=$('#commentText').val();
//     var parentId=$('#parentId').val();
//     console.log(comment);
//     console.log(parentId);

//     $.get('/articles/add-comment/article_comment/',{
//         article_comment: comment,
//         article_id: ArticleId,
//         parent_id: parentId

//     }).then(res=>{
//         // res(response is thing that recieve from url and endponin that send data.respone can be httpresponse-render-jsonresponse-filerespone and ...)
//         // console.log(res)

//         $('#comments_area').html(res)
//         $('#commentText').val('');
//         $('#parentId').val('');
        
//         //after adding comment must scroll to that 
//         if(parentId !== null && parentId !== ''){
//             document.getElementById('single_comment_'+parentId).scrollIntoView({behavior:'smooth'})
//         }else{
//             document.getElementById('comments_area').scrollIntoView({behavior:'smooth'})
//         }
//         // location.reload() // this reload the url and page and when use ajax we does not want that! so its useless

//     })
// }

// function fillParentId(parentId) {
//     $('#parentId').val(parentId);
//     document.getElementById('comment_form').scrollIntoView({behavior:'smooth'})
// }

