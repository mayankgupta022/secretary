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

            "notes/delNote/:id": "delNote",
            "notes/newNote": "newNote",
            "notes/note/:id": "note",
            "notes/restoreNote/:id": "restoreNote",
            "notes/trash": "notesTrash",
            "notes": "notes",
            "notes/:id": "notes",

            /**********/
            /* PAGES */
            /**********/
            "pages/delNotebook/:id": "delNotebook",
            "pages/delStack/:id": "delStack",
            "pages/makeDefaultNotebook/:id": "makeDefaultNotebook",
            "pages/newNotebook": "newNotebook",
            "pages/newStack": "newStack",
            "pages/notebook/:id": "notebook",
            "pages/notebooks": "notebooks",
            "pages/stack/:id": "stack",
            "pages/stacks": "stacks",
            "pages/delPage/:id": "delPage",
            "pages/newPage": "newPage",
            "pages/page/:id": "page",
            "pages/restorePage/:id": "restorePage",
            "pages/trash": "pagesTrash",
            "pages": "pages",
            "pages/:id": "pages",

            /**********/
            /* DIARY */
            /**********/
            "diary": "events",//done
            "diary/event/:id": "event",//done
            "diary/day/:id": "day",
            "diary/delDay/:id": "delDay",
            "diary/delCalender/:id": "delCalender",
            "diary/delEvent/:id": "delEvent",
            "diary/makeDefaultCalender/:id": "makeDefaultCalender",
            "diary/newDay": "newDay",
            "diary/newCalender": "newCalender",
            "diary/newEvent": "newEvent",
            "diary/calender/:id": "calender",
            "diary/calenders": "calenders",
            "diary/restoreEvent/:id": "restoreEvent",
            "diary/trash": "trash",
            "diary/:id": "diaryEvents"//done
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
        },

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

/**********/
/* PAGES */
/**********/

        delNotebook: function (id) {
            var self = this;
            require(["pagesDelNotebook/views/delNotebook"], function (DelNotebookView) {
                var delNotebookView = new DelNotebookView();
                self.updateCurrentView(delNotebookView);
                $(delNotebookView.render(id).el).appendTo($content);
            });
        },

        newNotebook: function () {
            var self = this;
            require(["pagesNewNotebook/views/newNotebook"], function (NewNotebookView) {
                var newNotebookView = new NewNotebookView();
                self.updateCurrentView(newNotebookView);
                $(newNotebookView.render().el).appendTo($content);
            });
        },

        delStack: function (id) {
            var self = this;
            require(["pagesDelStack/views/delStack"], function (DelStackView) {
                var delStackView = new DelStackView();
                self.updateCurrentView(delStackView);
                $(delStackView.render(id).el).appendTo($content);
            });
        },

        newStack: function () {
            var self = this;
            require(["pagesNewStack/views/newStack"], function (NewStackView) {
                var newStackView = new NewStackView();
                self.updateCurrentView(newStackView);
                $(newStackView.render().el).appendTo($content);
            });
        },

        makeDefaultNotebook: function (id) {
            var self = this;
            require(["pagesMakeDefaultNotebook/views/makeDefaultNotebook"], function (MakeDefaultNotebookView) {
                var makeDefaultNotebookView = new MakeDefaultNotebookView();
                self.updateCurrentView(makeDefaultNotebookView);
                $(makeDefaultNotebookView.render(id).el).appendTo($content);
            });
        },

        notebook: function (id) {
            var self = this;
            require(["pagesNotebook/views/notebook"], function (NotebookView) {
                var notebookView = new NotebookView();
                self.updateCurrentView(notebookView);
                $(notebookView.render(menuView, id).el).appendTo($content);
            });
        },

        notebooks: function () {

            var self = this;
            require(["pagesNotebooks/views/notebooks"], function (NotebooksView) {
                var notebooksView = new NotebooksView();
                self.updateCurrentView(notebooksView);
                $(notebooksView.render(menuView).el).appendTo($content);
            });
        },

        stack: function (id) {
            var self = this;
            require(["pagesStack/views/stack"], function (StackView) {
                var stackView = new StackView();
                self.updateCurrentView(stackView);
                $(stackView.render(menuView, id).el).appendTo($content);
            });
        },

        stacks: function () {

            var self = this;
            require(["pagesStacks/views/stacks"], function (StacksView) {
                var stacksView = new StacksView();
                self.updateCurrentView(stacksView);
                $(stacksView.render(menuView).el).appendTo($content);
            });
        },

        delPage: function (id) {
            var self = this;
            require(["pagesDel/views/delPage"], function (DelPageView) {
                var delPageView = new DelPageView();
                self.updateCurrentView(delPageView);
                $(delPageView.render(id).el).appendTo($content);
            });
        },

        newPage: function () {
            var self = this;
            require(["pagesNew/views/newPage"], function (NewPageView) {
                var newPageView = new NewPageView();
                self.updateCurrentView(newPageView);
                $(newPageView.render().el).appendTo($content);
            });
        },

        page: function (id) {
            var self = this;
            require(["pagesPage/views/page"], function (PageView) {
                var pageView = new PageView();
                self.updateCurrentView(pageView);
                $(pageView.render(menuView, id).el).appendTo($content);
            });
        },

        pages: function (id) {

            if(!id)
                id = 0;
            var self = this;
            require(["pages/views/pages"], function (PagesView) {
                var pagesView = new PagesView();
                self.updateCurrentView(pagesView);
                $(pagesView.render(menuView, id).el).appendTo($content);
            });
        },

        restorePage: function (id) {
            var self = this;
            require(["pagesRestore/views/restorePage"], function (RestorePageView) {
                var restorePageView = new RestorePageView();
                self.updateCurrentView(restorePageView);
                $(restorePageView.render(id).el).appendTo($content);
            });
        },

        pagesTrash: function () {
            var self = this;
            require(["pagesTrash/views/trash"], function (PagesTrashView) {
                var pagesTrashView = new PagesTrashView();
                self.updateCurrentView(pagesTrashView);
                $(pagesTrashView.render(menuView).el).appendTo($content);
            });
        },

/**********/
/* DIARY */
/**********/

        event: function (id) {
            var self = this;
            require(["diaryEvent/views/event"], function (EventView) {
                var eventView = new EventView();
                self.updateCurrentView(eventView);
                $(eventView.render(menuView, id).el).appendTo($content);
            });
        },

        delEvent: function (id) {
            var self = this;
            require(["diaryDelEvent/views/delEvent"], function (DelEventView) {
                var delEventView = new DelEventView();
                self.updateCurrentView(delEventView);
                $(delEventView.render(id).el).appendTo($content);
            });
        },

        newEvent: function () {
            var self = this;
            require(["diaryNewEvent/views/newEvent"], function (NewEventView) {
                var newEventView = new NewEventView();
                self.updateCurrentView(newEventView);
                $(newEventView.render().el).appendTo($content);
            });
        },

        events: function (id) {

            if(!id)
                id = 0;
            var self = this;
            require(["diaryEvents/views/events"], function (EventsView) {
                var eventsView = new EventsView();
                self.updateCurrentView(eventsView);
                $(eventsView.render(menuView, id).el).appendTo($content);
            });
        }

    });

});