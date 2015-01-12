define(function (require) {

    "use strict";

    var model       = require('common/models/model'),
        ShellView   = require('shell/views/shell'),
        MenuView    = require('menu/views/menu'),
        $body       = $('body'),
        shellView,
        menuView,
        currentView,
        $content;

    return Backbone.Router.extend({

        routes: {

            /**********/
            /* COMMON */
            /**********/

            "": "home",
            "blank": "blank",
            "try/:id": "try",

            /**********/
            /* USER */
            /**********/

            "changePass": "changePass",
            "login": "login",
            "logout": "logout",
            "signUp": "signUp",
            "updateInfo": "updateInfo",

            /**********/
            /* NOTES */
            /**********/

            "notes": "notes",
            "notes/:id": "notes",
            "notes/delNote/:id": "delNote",
            "notes/newNote": "newNote",
            "notes/note/:id": "note",
            "notes/restoreNote/:id": "restoreNote",
            "notes/trash": "notesTrash"
        },

/**********/
/* COMMON */
/**********/
        initialize: function () {

            this.listenTo(this, "route", this.getInfo);

            shellView = new ShellView();
            $body.html(shellView.render().el);
            $content = $("#content");
            menuView = new MenuView({el: $content});
        },

        blank: function () {
            document.router.navigate("", {trigger: true, replace: true});//replace: true required if history not to be maintained
        },

        home: function () {
            var self = this;
            require(["home/views/home"], function (HomeView) {
                var homeView = new HomeView();
                self.updateCurrentView(homeView);
                $(homeView.render(menuView).el).appendTo($content);
            });
        },

        try: function (id) {
            console.log(id);
        },

        getInfo: function() {
            var getInfo = new model.GetInfo();
            getInfo.fetch({
                        success: function (data) {
                            document.user = data.attributes.user;
                            document.firstName = data.attributes.firstName;
                            document.lastName = data.attributes.lastName;
                            document.email = data.attributes.email;
                            document.role = data.attributes.role;
                        },
                        error: function (data) {
                            document.user = 'anon';
                            document.firstName = 'Anon';
                            document.lastName = '';
                            document.role = 0;
                        }
                });
        },

        updateCurrentView: function(newView) {
            //COMPLETELY UNBIND THE VIEW
            if(this.currentView) {
                this.currentView.undelegateEvents();
                $(this.currentView.el).removeData().unbind(); 
                //Remove currentView from DOM
                this.currentView.remove();  
                Backbone.View.prototype.remove.call(this.currentView);

            }
            this.currentView=newView;
            this.currentView.delegateEvents(); // delegate events when the view is recycled
        }

/**********/
/* USER */
/**********/

        changePass: function () {
            var self = this;
            require(["changePass/views/changePass"], function (ChangePassView) {
                var changePassView = new ChangePassView();
                self.updateCurrentView(changePassView);
                $(changePassView.render(menuView).el).appendTo($content);
            });
        },

        login: function () {
            var self = this;
            require(["login/views/login"], function (LoginView) {
                var loginView = new LoginView();
                self.updateCurrentView(loginView);
                $(loginView.render(menuView).el).appendTo($content);
            });
        },

        logout: function () {
            var self = this;
            require(["logout/views/logout"], function (LogoutView) {
                var logoutView = new LogoutView();
                self.updateCurrentView(logoutView);
                $(logoutView.render().el).appendTo($content);
            });
        },

        signUp: function () {
            var self = this;
            require(["signUp/views/signUp"], function (SignUpView) {
                var signUpView = new SignUpView();
                self.updateCurrentView(signUpView);
                $(signUpView.render(menuView).el).appendTo($content);
            });
        },

        updateInfo: function () {
            var self = this;
            require(["updateInfo/views/updateInfo"], function (UpdateInfoView) {
                var updateInfoView = new UpdateInfoView();
                self.updateCurrentView(updateInfoView);
                $(updateInfoView.render(menuView).el).appendTo($content);
            });
        },

/**********/
/* NOTES */
/**********/

        delNote: function (id) {
            var self = this;
            require(["notesDel/views/delNote"], function (DelNoteView) {
                var delNoteView = new DelNoteView();
                self.updateCurrentView(delNoteView);
                $(delNoteView.render(id).el).appendTo($content);
            });
        },

        newNote: function () {
            var self = this;
            require(["notesNew/views/newNote"], function (NewNoteView) {
                var newNoteView = new NewNoteView();
                self.updateCurrentView(newNoteView);
                $(newNoteView.render().el).appendTo($content);
            });
        },

        note: function (id) {
            var self = this;
            require(["notesNote/views/note"], function (NoteView) {
                var noteView = new NoteView();
                self.updateCurrentView(noteView);
                $(noteView.render(menuView, id).el).appendTo($content);
            });
        },

        notes: function (id) {

            if(!id)
                id = 0;
            var self = this;
            require(["notes/views/notes"], function (NotesView) {
                var notesView = new NotesView();
                self.updateCurrentView(notesView);
                $(notesView.render(menuView, id).el).appendTo($content);
            });
        },

        restoreNote: function (id) {
            var self = this;
            require(["notesRestore/views/restoreNote"], function (RestoreNoteView) {
                var restoreNoteView = new RestoreNoteView();
                self.updateCurrentView(restoreNoteView);
                $(restoreNoteView.render(id).el).appendTo($content);
            });
        },

        notesTrash: function () {
            var self = this;
            require(["notesTrash/views/trash"], function (NotesTrashView) {
                var notesTrashView = new NotesTrashView();
                self.updateCurrentView(notesTrashView);
                $(notesTrashView.render(menuView).el).appendTo($content);
            });
        },

    });

});