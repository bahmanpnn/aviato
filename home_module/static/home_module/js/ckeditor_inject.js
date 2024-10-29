// // static/your_app/js/ckeditor_inject.js

// CKEDITOR.plugins.add('insertTitle', {
//     init: function(editor) {
//         editor.addCommand('insertTitle', {
//             exec: function(editor) {
//                 const titlePlaceholder = '{{ slider.title }}'; // No quotes around the placeholder itself
//                 const selection = editor.getSelection();
//                 const range = selection.getRanges()[0];

//                 // Insert the title placeholder at the cursor position
//                 range.insertNode(new CKEDITOR.dom.text(titlePlaceholder));
//                 range.select();
//             }
//         });

//         editor.ui.addButton('InsertTitle', {
//             label: 'Insert Title Placeholder',
//             command: 'insertTitle',
//             toolbar: 'insert'
//         });
//     }
});