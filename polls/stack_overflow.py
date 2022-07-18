html = '''
<html itemscope="" itemtype="https://schema.org/QAPage" class="html__responsive " lang="en"><head>

        <title>python - How can I get my Django server to reload when I change the HTML in dev mode without clicking the refresh button? - Stack Overflow</title>
        <link rel="shortcut icon" href="https://cdn.sstatic.net/Sites/stackoverflow/Img/favicon.ico?v=ec617d715196">
        <link rel="apple-touch-icon" href="https://cdn.sstatic.net/Sites/stackoverflow/Img/apple-touch-icon.png?v=c78bd457575a">
        <link rel="image_src" href="https://cdn.sstatic.net/Sites/stackoverflow/Img/apple-touch-icon.png?v=c78bd457575a">
        <link rel="search" type="application/opensearchdescription+xml" title="Stack Overflow" href="/opensearch.xml">
        <link rel="canonical" href="https://stackoverflow.com/questions/73013700/how-can-i-get-my-django-server-to-reload-when-i-change-the-html-in-dev-mode-with">
    <meta name="viewport" content="width=device-width, height=device-height, initial-scale=1.0, minimum-scale=1.0">
        <meta property="og:type" content="website">
        <meta property="og:url" content="https://stackoverflow.com/questions/73013700/how-can-i-get-my-django-server-to-reload-when-i-change-the-html-in-dev-mode-with">
        <meta property="og:site_name" content="Stack Overflow">
        <meta property="og:image" itemprop="image primaryImageOfPage" content="https://cdn.sstatic.net/Sites/stackoverflow/Img/apple-touch-icon@2.png?v=73d79a89bded">
        <meta name="twitter:card" content="summary">
        <meta name="twitter:domain" content="stackoverflow.com">
        <meta name="twitter:title" property="og:title" itemprop="name" content="How can I get my Django server to reload when I change the HTML in dev mode without clicking the refresh button?">
        <meta name="twitter:description" property="og:description" itemprop="description" content="I'm working on a Django project. Right now (if you're the dev) you can make changes to the HTML pretty easily. i'm not having any issues with that, i just want to know how to get the server to reload ">
    <script id="webpack-public-path" type="text/uri-list">https://cdn.sstatic.net/</script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <script async="" src="https://cdn.sstatic.net/Js/third-party/npm/@stackoverflow/stacks/dist/js/stacks.min.js?v=6cc27826a5fd"></script>
    <script src="https://cdn.sstatic.net/Js/stub.en.js?v=e6d116cd69f1"></script>


    <link rel="stylesheet" type="text/css" href="https://cdn.sstatic.net/Shared/stacks.css?v=3bbf3c79def9">
    <link rel="stylesheet" type="text/css" href="https://cdn.sstatic.net/Sites/stackoverflow/primary.css?v=05792009f5ef">



            <link rel="alternate" type="application/atom+xml" title="Feed for question 'How can I get my Django server to reload when I change the HTML in dev mode without clicking the refresh button?'" href="/feeds/question/73013700">
            <meta name="twitter:app:country" content="US">
            <meta name="twitter:app:name:iphone" content="Stack Exchange iOS">
            <meta name="twitter:app:id:iphone" content="871299723">
            <meta name="twitter:app:url:iphone" content="se-zaphod://stackoverflow.com/questions/73013700/how-can-i-get-my-django-server-to-reload-when-i-change-the-html-in-dev-mode-with/73013747">
            <meta name="twitter:app:name:ipad" content="Stack Exchange iOS">
            <meta name="twitter:app:id:ipad" content="871299723">
            <meta name="twitter:app:url:ipad" content="se-zaphod://stackoverflow.com/questions/73013700/how-can-i-get-my-django-server-to-reload-when-i-change-the-html-in-dev-mode-with/73013747">
            <meta name="twitter:app:name:googleplay" content="Stack Exchange Android">
            <meta name="twitter:app:url:googleplay" content="https://stackoverflow.com/questions/73013700/how-can-i-get-my-django-server-to-reload-when-i-change-the-html-in-dev-mode-with/73013747">
            <meta name="twitter:app:id:googleplay" content="com.stackexchange.marvin">
        <script>
            StackExchange.ready(function () {

                    StackExchange.using("snippets", function () {
                        StackExchange.snippets.initSnippetRenderer();
                    });

                StackExchange.using("postValidation", function () {
                    StackExchange.postValidation.initOnBlurAndSubmit($('#post-form'), 2, 'answer');
                });


                StackExchange.question.init({showAnswerHelp:true,showTrendingSortLaunchPopover:true,showTrendingSortPostLaunchPopover:false,totalCommentCount:0,shownCommentCount:0,enableTables:true,questionId:73013700});

                styleCode();

                    StackExchange.realtime.subscribeToQuestion('1', '73013700');
                    StackExchange.using("gps", function () { StackExchange.gps.trackOutboundClicks('#content', '.js-post-body'); });


            });
        </script>




        <link rel="stylesheet" type="text/css" href="https://cdn.sstatic.net/Shared/Channels/channels.css?v=f039f0b977b7">





    <script type="application/json" data-role="module-args" data-module-name="Shared/options.mod">{"options":{"locale":"en","serverTime":1658078723,"routeName":"Questions/Show","stackAuthUrl":"https://stackauth.com","networkMetaHostname":"meta.stackexchange.com","site":{"name":"Stack Overflow","description":"Q\u0026A for professional and enthusiast programmers","isNoticesTabEnabled":true,"enableNewTagCreationWarning":true,"insertSpaceAfterNameTabCompletion":false,"id":1,"cookieDomain":".stackoverflow.com","childUrl":"https://meta.stackoverflow.com","negativeVoteScoreFloor":null,"enableSocialMediaInSharePopup":true,"protocol":"https"},"user":{"fkey":"a1652ef8742c146baba5659e062cb0b54f183b9d298ed240b4cdb062a0535d03","tid":"e83c5819-1605-7705-750b-aa42868877a9","rep":0,"isAnonymous":true,"isAnonymousNetworkWide":true},"events":{"postType":{"question":1},"postEditionSection":{"title":1,"body":2,"tags":3}},"svgIconPath":"https://cdn.sstatic.net/Img/stacks-icons","svgIconHash":"e07884e71a43"}}</script>
<script type="application/json" data-role="module-args" data-module-name="Shared/settings.mod">{"settings":{"userMessaging":{"showNewFeatureNotice":true},"tags":{},"subscriptions":{"defaultBasicMaxTrueUpSeats":250,"defaultFreemiumMaxTrueUpSeats":50,"defaultMaxTrueUpSeats":1000},"snippets":{"renderDomain":"stacksnippets.net","snippetsEnabled":true},"site":{"allowImageUploads":true,"enableImgurHttps":true,"enableUserHovercards":true,"forceHttpsImages":true,"styleCode":true},"questions":{"enableQuestionTitleLengthLiveWarning":true,"maxTitleSize":150,"questionTitleLengthStartLiveWarningChars":50},"intercom":{"appId":"inf0secd","hostBaseUrl":"https://stacksnippets.net"},"paths":{},"monitoring":{"clientTimingsAbsoluteTimeout":30000,"clientTimingsDebounceTimeout":1000},"mentions":{"maxNumUsersInDropdown":50},"markdown":{"enableTables":true},"legal":{"oneTrustConfigId":"c3d9f1e3-55f3-4eba-b268-46cee4c6789c"},"flags":{"allowRetractingCommentFlags":true,"allowRetractingFlags":true},"elections":{"opaVoteResultsBaseUrl":"https://www.opavote.com/results/"},"comments":{},"accounts":{"currentPasswordRequiredForChangingStackIdPassword":true}}}</script>
<script>StackExchange.init();</script>

    <script>
        StackExchange.using.setCacheBreakers({"Js/adops.en.js":"6da43f5e0a84","Js/ask.en.js":"7ff9a9068fd6","Js/begin-edit-event.en.js":"dd955babf04d","Js/copy-transpiled.en.js":"e7855bee94f2","Js/events.en.js":"","Js/explore-qlist.en.js":"2b1f34938b8b","Js/full-anon.en.js":"f2312e2f4665","Js/full.en.js":"39bd993bf30d","Js/highlightjs-loader.en.js":"a284064706b3","Js/inline-tag-editing.en.js":"77f922e6e562","Js/keyboard-shortcuts.en.js":"fa78d9020f1f","Js/markdown-it-loader.en.js":"5818ef89ff9d","Js/moderator.en.js":"df5a2eb14f4c","Js/postCollections-transpiled.en.js":"529276cfb7ae","Js/post-validation.en.js":"5dfbf70d3623","Js/question-editor.en.js":"","Js/review-v2-transpiled.en.js":"d5efdefd09e8","Js/revisions.en.js":"a86490719687","Js/stacks-editor.en.js":"230f551098fb","Js/tageditor.en.js":"825c9597ce2d","Js/tageditornew.en.js":"126f7e015aea","Js/tagsuggestions.en.js":"1bcff7d98f97","Js/unlimited-transpiled.en.js":"7ed67670b600","Js/wmd.en.js":"7014572a759f","Js/snippet-javascript-codemirror.en.js":"73fce5cc7219"});
        StackExchange.using("gps", function() {
             StackExchange.gps.init(false);
        });
    </script>
    <noscript id="noscript-css"><style>body,.s-topbar{margin-top:1.9em}</style></noscript>
    <script async="" src="https://cdn.sstatic.net/Js/full-anon.en.js?v=f2312e2f4665"></script><script async="" src="https://cdn.sstatic.net/Js/post-validation.en.js?v=5dfbf70d3623"></script><script src="https://cdn.cookielaw.org/scripttemplates/6.37.0/otBannerSdk.js" async="" type="text/javascript"></script><div id="onetrust-style" class="d-none">#onetrust-banner-sdk{-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%}#onetrust-banner-sdk .onetrust-vendors-list-handler{cursor:pointer;color:#1f96db;font-size:inherit;font-weight:bold;text-decoration:none;margin-left:5px}#onetrust-banner-sdk .onetrust-vendors-list-handler:hover{color:#1f96db}#onetrust-banner-sdk:focus{outline:2px solid #000;outline-offset:-2px}#onetrust-banner-sdk a:focus{outline:2px solid #000}#onetrust-banner-sdk #onetrust-accept-btn-handler,#onetrust-banner-sdk #onetrust-reject-all-handler,#onetrust-banner-sdk #onetrust-pc-btn-handler{outline-offset:1px}#onetrust-banner-sdk.ot-bnr-w-logo .ot-bnr-logo{height:64px;width:64px}#onetrust-banner-sdk .ot-close-icon,#onetrust-pc-sdk .ot-close-icon,#ot-sync-ntfy .ot-close-icon{background-image:url("data:image/svg+xml;base64,PHN2ZyB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHg9IjBweCIgeT0iMHB4IiB3aWR0aD0iMzQ4LjMzM3B4IiBoZWlnaHQ9IjM0OC4zMzNweCIgdmlld0JveD0iMCAwIDM0OC4zMzMgMzQ4LjMzNCIgc3R5bGU9ImVuYWJsZS1iYWNrZ3JvdW5kOm5ldyAwIDAgMzQ4LjMzMyAzNDguMzM0OyIgeG1sOnNwYWNlPSJwcmVzZXJ2ZSI+PGc+PHBhdGggZmlsbD0iIzU2NTY1NiIgZD0iTTMzNi41NTksNjguNjExTDIzMS4wMTYsMTc0LjE2NWwxMDUuNTQzLDEwNS41NDljMTUuNjk5LDE1LjcwNSwxNS42OTksNDEuMTQ1LDAsNTYuODVjLTcuODQ0LDcuODQ0LTE4LjEyOCwxMS43NjktMjguNDA3LDExLjc2OWMtMTAuMjk2LDAtMjAuNTgxLTMuOTE5LTI4LjQxOS0xMS43NjlMMTc0LjE2NywyMzEuMDAzTDY4LjYwOSwzMzYuNTYzYy03Ljg0Myw3Ljg0NC0xOC4xMjgsMTEuNzY5LTI4LjQxNiwxMS43NjljLTEwLjI4NSwwLTIwLjU2My0zLjkxOS0yOC40MTMtMTEuNzY5Yy0xNS42OTktMTUuNjk4LTE1LjY5OS00MS4xMzksMC01Ni44NWwxMDUuNTQtMTA1LjU0OUwxMS43NzQsNjguNjExYy0xNS42OTktMTUuNjk5LTE1LjY5OS00MS4xNDUsMC01Ni44NDRjMTUuNjk2LTE1LjY4Nyw0MS4xMjctMTUuNjg3LDU2LjgyOSwwbDEwNS41NjMsMTA1LjU1NEwyNzkuNzIxLDExLjc2N2MxNS43MDUtMTUuNjg3LDQxLjEzOS0xNS42ODcsNTYuODMyLDBDMzUyLjI1OCwyNy40NjYsMzUyLjI1OCw1Mi45MTIsMzM2LjU1OSw2OC42MTF6Ii8+PC9nPjwvc3ZnPg==");background-size:contain;background-repeat:no-repeat;background-position:center;height:12px;width:12px}#onetrust-banner-sdk .powered-by-logo,#onetrust-banner-sdk .ot-pc-footer-logo a,#onetrust-pc-sdk .powered-by-logo,#onetrust-pc-sdk .ot-pc-footer-logo a,#ot-sync-ntfy .powered-by-logo,#ot-sync-ntfy .ot-pc-footer-logo a{background-size:contain;background-repeat:no-repeat;background-position:center;height:25px;width:152px;display:block;text-decoration:none;font-size:0.75em}#onetrust-banner-sdk .powered-by-logo:hover,#onetrust-banner-sdk .ot-pc-footer-logo a:hover,#onetrust-pc-sdk .powered-by-logo:hover,#onetrust-pc-sdk .ot-pc-footer-logo a:hover,#ot-sync-ntfy .powered-by-logo:hover,#ot-sync-ntfy .ot-pc-footer-logo a:hover{color:#565656}#onetrust-banner-sdk h3 *,#onetrust-banner-sdk h4 *,#onetrust-banner-sdk h6 *,#onetrust-banner-sdk button *,#onetrust-banner-sdk a[data-parent-id] *,#onetrust-pc-sdk h3 *,#onetrust-pc-sdk h4 *,#onetrust-pc-sdk h6 *,#onetrust-pc-sdk button *,#onetrust-pc-sdk a[data-parent-id] *,#ot-sync-ntfy h3 *,#ot-sync-ntfy h4 *,#ot-sync-ntfy h6 *,#ot-sync-ntfy button *,#ot-sync-ntfy a[data-parent-id] *{font-size:inherit;font-weight:inherit;color:inherit}#onetrust-banner-sdk .ot-hide,#onetrust-pc-sdk .ot-hide,#ot-sync-ntfy .ot-hide{display:none !important}#onetrust-banner-sdk button.ot-link-btn:hover,#onetrust-pc-sdk button.ot-link-btn:hover,#ot-sync-ntfy button.ot-link-btn:hover{text-decoration:underline;opacity:1}#onetrust-pc-sdk .ot-sdk-row .ot-sdk-column{padding:0}#onetrust-pc-sdk .ot-sdk-container{padding-right:0}#onetrust-pc-sdk .ot-sdk-row{flex-direction:initial;width:100%}#onetrust-pc-sdk [type="checkbox"]:checked,#onetrust-pc-sdk [type="checkbox"]:not(:checked){pointer-events:initial}#onetrust-pc-sdk [type="checkbox"]:disabled+label::before,#onetrust-pc-sdk [type="checkbox"]:disabled+label:after,#onetrust-pc-sdk [type="checkbox"]:disabled+label{pointer-events:none;opacity:0.7}#onetrust-pc-sdk #vendor-list-content{transform:translate3d(0, 0, 0)}#onetrust-pc-sdk li input[type="checkbox"]{z-index:1}#onetrust-pc-sdk li .ot-checkbox label{z-index:2}#onetrust-pc-sdk li .ot-checkbox input[type="checkbox"]{height:auto;width:auto}#onetrust-pc-sdk li .host-title a,#onetrust-pc-sdk li .ot-host-name a,#onetrust-pc-sdk li .accordion-text,#onetrust-pc-sdk li .ot-acc-txt{z-index:2;position:relative}#onetrust-pc-sdk input{margin:3px 0.1ex}#onetrust-pc-sdk .pc-logo,#onetrust-pc-sdk .ot-pc-logo{height:60px;width:180px;background-position:center;background-size:contain;background-repeat:no-repeat}#onetrust-pc-sdk .screen-reader-only,#onetrust-pc-sdk .ot-scrn-rdr,.ot-sdk-cookie-policy .screen-reader-only,.ot-sdk-cookie-policy .ot-scrn-rdr{border:0;clip:rect(0 0 0 0);height:1px;margin:-1px;overflow:hidden;padding:0;position:absolute;width:1px}#onetrust-pc-sdk.ot-fade-in,.onetrust-pc-dark-filter.ot-fade-in,#onetrust-banner-sdk.ot-fade-in{animation-name:onetrust-fade-in;animation-duration:400ms;animation-timing-function:ease-in-out}#onetrust-pc-sdk.ot-hide{display:none !important}.onetrust-pc-dark-filter.ot-hide{display:none !important}#ot-sdk-btn.ot-sdk-show-settings,#ot-sdk-btn.optanon-show-settings{color:#68b631;border:1px solid #68b631;height:auto;white-space:normal;word-wrap:break-word;padding:0.8em 2em;font-size:0.8em;line-height:1.2;cursor:pointer;-moz-transition:0.1s ease;-o-transition:0.1s ease;-webkit-transition:1s ease;transition:0.1s ease}#ot-sdk-btn.ot-sdk-show-settings:hover,#ot-sdk-btn.optanon-show-settings:hover{color:#fff;background-color:#68b631}.onetrust-pc-dark-filter{background:rgba(0,0,0,0.5);z-index:2147483646;width:100%;height:100%;overflow:hidden;position:fixed;top:0;bottom:0;left:0}@keyframes onetrust-fade-in{0%{opacity:0}100%{opacity:1}}.ot-cookie-label{text-decoration:underline}@media only screen and (min-width: 426px) and (max-width: 896px) and (orientation: landscape){#onetrust-pc-sdk p{font-size:0.75em}}#onetrust-banner-sdk .banner-option-input:focus+label{outline:1px solid #000;outline-style:auto}.category-vendors-list-handler+a:focus,.category-vendors-list-handler+a:focus-visible{outline:2px solid #000}#onetrust-pc-sdk .ot-userid-title{margin-top:10px}#onetrust-pc-sdk .ot-userid-title&gt;span,#onetrust-pc-sdk .ot-userid-timestamp&gt;span{font-weight:700}#onetrust-pc-sdk .ot-userid-desc{font-style:italic}#onetrust-pc-sdk .ot-host-desc a{pointer-events:initial}#onetrust-pc-sdk .ot-ven-hdr&gt;p a{position:relative;z-index:2;pointer-events:initial}#onetrust-pc-sdk .ot-vnd-serv .ot-vnd-item .ot-vnd-info a,#onetrust-pc-sdk .ot-vs-list .ot-vnd-item .ot-vnd-info a{margin-right:auto}
#onetrust-banner-sdk,#onetrust-pc-sdk,#ot-sdk-cookie-policy,#ot-sync-ntfy{font-size:16px}#onetrust-banner-sdk *,#onetrust-banner-sdk ::after,#onetrust-banner-sdk ::before,#onetrust-pc-sdk *,#onetrust-pc-sdk ::after,#onetrust-pc-sdk ::before,#ot-sdk-cookie-policy *,#ot-sdk-cookie-policy ::after,#ot-sdk-cookie-policy ::before,#ot-sync-ntfy *,#ot-sync-ntfy ::after,#ot-sync-ntfy ::before{-webkit-box-sizing:content-box;-moz-box-sizing:content-box;box-sizing:content-box}#onetrust-banner-sdk div,#onetrust-banner-sdk span,#onetrust-banner-sdk h1,#onetrust-banner-sdk h2,#onetrust-banner-sdk h3,#onetrust-banner-sdk h4,#onetrust-banner-sdk h5,#onetrust-banner-sdk h6,#onetrust-banner-sdk p,#onetrust-banner-sdk img,#onetrust-banner-sdk svg,#onetrust-banner-sdk button,#onetrust-banner-sdk section,#onetrust-banner-sdk a,#onetrust-banner-sdk label,#onetrust-banner-sdk input,#onetrust-banner-sdk ul,#onetrust-banner-sdk li,#onetrust-banner-sdk nav,#onetrust-banner-sdk table,#onetrust-banner-sdk thead,#onetrust-banner-sdk tr,#onetrust-banner-sdk td,#onetrust-banner-sdk tbody,#onetrust-banner-sdk .ot-main-content,#onetrust-banner-sdk .ot-toggle,#onetrust-banner-sdk #ot-content,#onetrust-banner-sdk #ot-pc-content,#onetrust-banner-sdk .checkbox,#onetrust-pc-sdk div,#onetrust-pc-sdk span,#onetrust-pc-sdk h1,#onetrust-pc-sdk h2,#onetrust-pc-sdk h3,#onetrust-pc-sdk h4,#onetrust-pc-sdk h5,#onetrust-pc-sdk h6,#onetrust-pc-sdk p,#onetrust-pc-sdk img,#onetrust-pc-sdk svg,#onetrust-pc-sdk button,#onetrust-pc-sdk section,#onetrust-pc-sdk a,#onetrust-pc-sdk label,#onetrust-pc-sdk input,#onetrust-pc-sdk ul,#onetrust-pc-sdk li,#onetrust-pc-sdk nav,#onetrust-pc-sdk table,#onetrust-pc-sdk thead,#onetrust-pc-sdk tr,#onetrust-pc-sdk td,#onetrust-pc-sdk tbody,#onetrust-pc-sdk .ot-main-content,#onetrust-pc-sdk .ot-toggle,#onetrust-pc-sdk #ot-content,#onetrust-pc-sdk #ot-pc-content,#onetrust-pc-sdk .checkbox,#ot-sdk-cookie-policy div,#ot-sdk-cookie-policy span,#ot-sdk-cookie-policy h1,#ot-sdk-cookie-policy h2,#ot-sdk-cookie-policy h3,#ot-sdk-cookie-policy h4,#ot-sdk-cookie-policy h5,#ot-sdk-cookie-policy h6,#ot-sdk-cookie-policy p,#ot-sdk-cookie-policy img,#ot-sdk-cookie-policy svg,#ot-sdk-cookie-policy button,#ot-sdk-cookie-policy section,#ot-sdk-cookie-policy a,#ot-sdk-cookie-policy label,#ot-sdk-cookie-policy input,#ot-sdk-cookie-policy ul,#ot-sdk-cookie-policy li,#ot-sdk-cookie-policy nav,#ot-sdk-cookie-policy table,#ot-sdk-cookie-policy thead,#ot-sdk-cookie-policy tr,#ot-sdk-cookie-policy td,#ot-sdk-cookie-policy tbody,#ot-sdk-cookie-policy .ot-main-content,#ot-sdk-cookie-policy .ot-toggle,#ot-sdk-cookie-policy #ot-content,#ot-sdk-cookie-policy #ot-pc-content,#ot-sdk-cookie-policy .checkbox,#ot-sync-ntfy div,#ot-sync-ntfy span,#ot-sync-ntfy h1,#ot-sync-ntfy h2,#ot-sync-ntfy h3,#ot-sync-ntfy h4,#ot-sync-ntfy h5,#ot-sync-ntfy h6,#ot-sync-ntfy p,#ot-sync-ntfy img,#ot-sync-ntfy svg,#ot-sync-ntfy button,#ot-sync-ntfy section,#ot-sync-ntfy a,#ot-sync-ntfy label,#ot-sync-ntfy input,#ot-sync-ntfy ul,#ot-sync-ntfy li,#ot-sync-ntfy nav,#ot-sync-ntfy table,#ot-sync-ntfy thead,#ot-sync-ntfy tr,#ot-sync-ntfy td,#ot-sync-ntfy tbody,#ot-sync-ntfy .ot-main-content,#ot-sync-ntfy .ot-toggle,#ot-sync-ntfy #ot-content,#ot-sync-ntfy #ot-pc-content,#ot-sync-ntfy .checkbox{font-family:inherit;font-weight:normal;-webkit-font-smoothing:auto;letter-spacing:normal;line-height:normal;padding:0;margin:0;height:auto;min-height:0;max-height:none;width:auto;min-width:0;max-width:none;border-radius:0;border:none;clear:none;float:none;position:static;bottom:auto;left:auto;right:auto;top:auto;text-align:left;text-decoration:none;text-indent:0;text-shadow:none;text-transform:none;white-space:normal;background:none;overflow:visible;vertical-align:baseline;visibility:visible;z-index:auto;box-shadow:none}#onetrust-banner-sdk label:before,#onetrust-banner-sdk label:after,#onetrust-banner-sdk .checkbox:after,#onetrust-banner-sdk .checkbox:before,#onetrust-pc-sdk label:before,#onetrust-pc-sdk label:after,#onetrust-pc-sdk .checkbox:after,#onetrust-pc-sdk .checkbox:before,#ot-sdk-cookie-policy label:before,#ot-sdk-cookie-policy label:after,#ot-sdk-cookie-policy .checkbox:after,#ot-sdk-cookie-policy .checkbox:before,#ot-sync-ntfy label:before,#ot-sync-ntfy label:after,#ot-sync-ntfy .checkbox:after,#ot-sync-ntfy .checkbox:before{content:"";content:none}
#onetrust-banner-sdk .ot-sdk-container,#onetrust-pc-sdk .ot-sdk-container,#ot-sdk-cookie-policy .ot-sdk-container{position:relative;width:100%;max-width:100%;margin:0 auto;padding:0 20px;box-sizing:border-box}#onetrust-banner-sdk .ot-sdk-column,#onetrust-banner-sdk .ot-sdk-columns,#onetrust-pc-sdk .ot-sdk-column,#onetrust-pc-sdk .ot-sdk-columns,#ot-sdk-cookie-policy .ot-sdk-column,#ot-sdk-cookie-policy .ot-sdk-columns{width:100%;float:left;box-sizing:border-box;padding:0;display:initial}@media (min-width: 400px){#onetrust-banner-sdk .ot-sdk-container,#onetrust-pc-sdk .ot-sdk-container,#ot-sdk-cookie-policy .ot-sdk-container{width:90%;padding:0}}@media (min-width: 550px){#onetrust-banner-sdk .ot-sdk-container,#onetrust-pc-sdk .ot-sdk-container,#ot-sdk-cookie-policy .ot-sdk-container{width:100%}#onetrust-banner-sdk .ot-sdk-column,#onetrust-banner-sdk .ot-sdk-columns,#onetrust-pc-sdk .ot-sdk-column,#onetrust-pc-sdk .ot-sdk-columns,#ot-sdk-cookie-policy .ot-sdk-column,#ot-sdk-cookie-policy .ot-sdk-columns{margin-left:4%}#onetrust-banner-sdk .ot-sdk-column:first-child,#onetrust-banner-sdk .ot-sdk-columns:first-child,#onetrust-pc-sdk .ot-sdk-column:first-child,#onetrust-pc-sdk .ot-sdk-columns:first-child,#ot-sdk-cookie-policy .ot-sdk-column:first-child,#ot-sdk-cookie-policy .ot-sdk-columns:first-child{margin-left:0}#onetrust-banner-sdk .ot-sdk-two.ot-sdk-columns,#onetrust-pc-sdk .ot-sdk-two.ot-sdk-columns,#ot-sdk-cookie-policy .ot-sdk-two.ot-sdk-columns{width:13.3333333333%}#onetrust-banner-sdk .ot-sdk-three.ot-sdk-columns,#onetrust-pc-sdk .ot-sdk-three.ot-sdk-columns,#ot-sdk-cookie-policy .ot-sdk-three.ot-sdk-columns{width:22%}#onetrust-banner-sdk .ot-sdk-four.ot-sdk-columns,#onetrust-pc-sdk .ot-sdk-four.ot-sdk-columns,#ot-sdk-cookie-policy .ot-sdk-four.ot-sdk-columns{width:30.6666666667%}#onetrust-banner-sdk .ot-sdk-eight.ot-sdk-columns,#onetrust-pc-sdk .ot-sdk-eight.ot-sdk-columns,#ot-sdk-cookie-policy .ot-sdk-eight.ot-sdk-columns{width:65.3333333333%}#onetrust-banner-sdk .ot-sdk-nine.ot-sdk-columns,#onetrust-pc-sdk .ot-sdk-nine.ot-sdk-columns,#ot-sdk-cookie-policy .ot-sdk-nine.ot-sdk-columns{width:74%}#onetrust-banner-sdk .ot-sdk-ten.ot-sdk-columns,#onetrust-pc-sdk .ot-sdk-ten.ot-sdk-columns,#ot-sdk-cookie-policy .ot-sdk-ten.ot-sdk-columns{width:82.6666666667%}#onetrust-banner-sdk .ot-sdk-eleven.ot-sdk-columns,#onetrust-pc-sdk .ot-sdk-eleven.ot-sdk-columns,#ot-sdk-cookie-policy .ot-sdk-eleven.ot-sdk-columns{width:91.3333333333%}#onetrust-banner-sdk .ot-sdk-twelve.ot-sdk-columns,#onetrust-pc-sdk .ot-sdk-twelve.ot-sdk-columns,#ot-sdk-cookie-policy .ot-sdk-twelve.ot-sdk-columns{width:100%;margin-left:0}}#onetrust-banner-sdk h1,#onetrust-banner-sdk h2,#onetrust-banner-sdk h3,#onetrust-banner-sdk h4,#onetrust-banner-sdk h5,#onetrust-banner-sdk h6,#onetrust-pc-sdk h1,#onetrust-pc-sdk h2,#onetrust-pc-sdk h3,#onetrust-pc-sdk h4,#onetrust-pc-sdk h5,#onetrust-pc-sdk h6,#ot-sdk-cookie-policy h1,#ot-sdk-cookie-policy h2,#ot-sdk-cookie-policy h3,#ot-sdk-cookie-policy h4,#ot-sdk-cookie-policy h5,#ot-sdk-cookie-policy h6{margin-top:0;font-weight:600;font-family:inherit}#onetrust-banner-sdk h1,#onetrust-pc-sdk h1,#ot-sdk-cookie-policy h1{font-size:1.5rem;line-height:1.2}#onetrust-banner-sdk h2,#onetrust-pc-sdk h2,#ot-sdk-cookie-policy h2{font-size:1.5rem;line-height:1.25}#onetrust-banner-sdk h3,#onetrust-pc-sdk h3,#ot-sdk-cookie-policy h3{font-size:1.5rem;line-height:1.3}#onetrust-banner-sdk h4,#onetrust-pc-sdk h4,#ot-sdk-cookie-policy h4{font-size:1.5rem;line-height:1.35}#onetrust-banner-sdk h5,#onetrust-pc-sdk h5,#ot-sdk-cookie-policy h5{font-size:1.5rem;line-height:1.5}#onetrust-banner-sdk h6,#onetrust-pc-sdk h6,#ot-sdk-cookie-policy h6{font-size:1.5rem;line-height:1.6}@media (min-width: 550px){#onetrust-banner-sdk h1,#onetrust-pc-sdk h1,#ot-sdk-cookie-policy h1{font-size:1.5rem}#onetrust-banner-sdk h2,#onetrust-pc-sdk h2,#ot-sdk-cookie-policy h2{font-size:1.5rem}#onetrust-banner-sdk h3,#onetrust-pc-sdk h3,#ot-sdk-cookie-policy h3{font-size:1.5rem}#onetrust-banner-sdk h4,#onetrust-pc-sdk h4,#ot-sdk-cookie-policy h4{font-size:1.5rem}#onetrust-banner-sdk h5,#onetrust-pc-sdk h5,#ot-sdk-cookie-policy h5{font-size:1.5rem}#onetrust-banner-sdk h6,#onetrust-pc-sdk h6,#ot-sdk-cookie-policy h6{font-size:1.5rem}}#onetrust-banner-sdk p,#onetrust-pc-sdk p,#ot-sdk-cookie-policy p{margin:0 0 1em 0;font-family:inherit;line-height:normal}#onetrust-banner-sdk a,#onetrust-pc-sdk a,#ot-sdk-cookie-policy a{color:#565656;text-decoration:underline}#onetrust-banner-sdk a:hover,#onetrust-pc-sdk a:hover,#ot-sdk-cookie-policy a:hover{color:#565656;text-decoration:none}#onetrust-banner-sdk .ot-sdk-button,#onetrust-banner-sdk button,#onetrust-pc-sdk .ot-sdk-button,#onetrust-pc-sdk button,#ot-sdk-cookie-policy .ot-sdk-button,#ot-sdk-cookie-policy button{margin-bottom:1rem;font-family:inherit}#onetrust-banner-sdk .ot-sdk-button,#onetrust-banner-sdk button,#onetrust-pc-sdk .ot-sdk-button,#onetrust-pc-sdk button,#ot-sdk-cookie-policy .ot-sdk-button,#ot-sdk-cookie-policy button{display:inline-block;height:38px;padding:0 30px;color:#555;text-align:center;font-size:0.9em;font-weight:400;line-height:38px;letter-spacing:0.01em;text-decoration:none;white-space:nowrap;background-color:transparent;border-radius:2px;border:1px solid #bbb;cursor:pointer;box-sizing:border-box}#onetrust-banner-sdk .ot-sdk-button:hover,#onetrust-banner-sdk :not(.ot-leg-btn-container)&gt;button:not(.ot-link-btn):hover,#onetrust-banner-sdk :not(.ot-leg-btn-container)&gt;button:not(.ot-link-btn):focus,#onetrust-pc-sdk .ot-sdk-button:hover,#onetrust-pc-sdk :not(.ot-leg-btn-container)&gt;button:not(.ot-link-btn):hover,#onetrust-pc-sdk :not(.ot-leg-btn-container)&gt;button:not(.ot-link-btn):focus,#ot-sdk-cookie-policy .ot-sdk-button:hover,#ot-sdk-cookie-policy :not(.ot-leg-btn-container)&gt;button:not(.ot-link-btn):hover,#ot-sdk-cookie-policy :not(.ot-leg-btn-container)&gt;button:not(.ot-link-btn):focus{color:#333;border-color:#888;opacity:0.7}#onetrust-banner-sdk .ot-sdk-button:focus,#onetrust-banner-sdk :not(.ot-leg-btn-container)&gt;button:focus,#onetrust-pc-sdk .ot-sdk-button:focus,#onetrust-pc-sdk :not(.ot-leg-btn-container)&gt;button:focus,#ot-sdk-cookie-policy .ot-sdk-button:focus,#ot-sdk-cookie-policy :not(.ot-leg-btn-container)&gt;button:focus{outline:2px solid #000}#onetrust-banner-sdk .ot-sdk-button.ot-sdk-button-primary,#onetrust-banner-sdk button.ot-sdk-button-primary,#onetrust-banner-sdk input[type="submit"].ot-sdk-button-primary,#onetrust-banner-sdk input[type="reset"].ot-sdk-button-primary,#onetrust-banner-sdk input[type="button"].ot-sdk-button-primary,#onetrust-pc-sdk .ot-sdk-button.ot-sdk-button-primary,#onetrust-pc-sdk button.ot-sdk-button-primary,#onetrust-pc-sdk input[type="submit"].ot-sdk-button-primary,#onetrust-pc-sdk input[type="reset"].ot-sdk-button-primary,#onetrust-pc-sdk input[type="button"].ot-sdk-button-primary,#ot-sdk-cookie-policy .ot-sdk-button.ot-sdk-button-primary,#ot-sdk-cookie-policy button.ot-sdk-button-primary,#ot-sdk-cookie-policy input[type="submit"].ot-sdk-button-primary,#ot-sdk-cookie-policy input[type="reset"].ot-sdk-button-primary,#ot-sdk-cookie-policy input[type="button"].ot-sdk-button-primary{color:#fff;background-color:#33c3f0;border-color:#33c3f0}#onetrust-banner-sdk .ot-sdk-button.ot-sdk-button-primary:hover,#onetrust-banner-sdk button.ot-sdk-button-primary:hover,#onetrust-banner-sdk input[type="submit"].ot-sdk-button-primary:hover,#onetrust-banner-sdk input[type="reset"].ot-sdk-button-primary:hover,#onetrust-banner-sdk input[type="button"].ot-sdk-button-primary:hover,#onetrust-banner-sdk .ot-sdk-button.ot-sdk-button-primary:focus,#onetrust-banner-sdk button.ot-sdk-button-primary:focus,#onetrust-banner-sdk input[type="submit"].ot-sdk-button-primary:focus,#onetrust-banner-sdk input[type="reset"].ot-sdk-button-primary:focus,#onetrust-banner-sdk input[type="button"].ot-sdk-button-primary:focus,#onetrust-pc-sdk .ot-sdk-button.ot-sdk-button-primary:hover,#onetrust-pc-sdk button.ot-sdk-button-primary:hover,#onetrust-pc-sdk input[type="submit"].ot-sdk-button-primary:hover,#onetrust-pc-sdk input[type="reset"].ot-sdk-button-primary:hover,#onetrust-pc-sdk input[type="button"].ot-sdk-button-primary:hover,#onetrust-pc-sdk .ot-sdk-button.ot-sdk-button-primary:focus,#onetrust-pc-sdk button.ot-sdk-button-primary:focus,#onetrust-pc-sdk input[type="submit"].ot-sdk-button-primary:focus,#onetrust-pc-sdk input[type="reset"].ot-sdk-button-primary:focus,#onetrust-pc-sdk input[type="button"].ot-sdk-button-primary:focus,#ot-sdk-cookie-policy .ot-sdk-button.ot-sdk-button-primary:hover,#ot-sdk-cookie-policy button.ot-sdk-button-primary:hover,#ot-sdk-cookie-policy input[type="submit"].ot-sdk-button-primary:hover,#ot-sdk-cookie-policy input[type="reset"].ot-sdk-button-primary:hover,#ot-sdk-cookie-policy input[type="button"].ot-sdk-button-primary:hover,#ot-sdk-cookie-policy .ot-sdk-button.ot-sdk-button-primary:focus,#ot-sdk-cookie-policy button.ot-sdk-button-primary:focus,#ot-sdk-cookie-policy input[type="submit"].ot-sdk-button-primary:focus,#ot-sdk-cookie-policy input[type="reset"].ot-sdk-button-primary:focus,#ot-sdk-cookie-policy input[type="button"].ot-sdk-button-primary:focus{color:#fff;background-color:#1eaedb;border-color:#1eaedb}#onetrust-banner-sdk input[type="text"],#onetrust-pc-sdk input[type="text"],#ot-sdk-cookie-policy input[type="text"]{height:38px;padding:6px 10px;background-color:#fff;border:1px solid #d1d1d1;border-radius:4px;box-shadow:none;box-sizing:border-box}#onetrust-banner-sdk input[type="text"],#onetrust-pc-sdk input[type="text"],#ot-sdk-cookie-policy input[type="text"]{-webkit-appearance:none;-moz-appearance:none;appearance:none}#onetrust-banner-sdk input[type="text"]:focus,#onetrust-pc-sdk input[type="text"]:focus,#ot-sdk-cookie-policy input[type="text"]:focus{border:1px solid #000;outline:0}#onetrust-banner-sdk label,#onetrust-pc-sdk label,#ot-sdk-cookie-policy label{display:block;margin-bottom:0.5rem;font-weight:600}#onetrust-banner-sdk input[type="checkbox"],#onetrust-pc-sdk input[type="checkbox"],#ot-sdk-cookie-policy input[type="checkbox"]{display:inline}#onetrust-banner-sdk ul,#onetrust-pc-sdk ul,#ot-sdk-cookie-policy ul{list-style:circle inside}#onetrust-banner-sdk ul,#onetrust-pc-sdk ul,#ot-sdk-cookie-policy ul{padding-left:0;margin-top:0}#onetrust-banner-sdk ul ul,#onetrust-pc-sdk ul ul,#ot-sdk-cookie-policy ul ul{margin:1.5rem 0 1.5rem 3rem;font-size:90%}#onetrust-banner-sdk li,#onetrust-pc-sdk li,#ot-sdk-cookie-policy li{margin-bottom:1rem}#onetrust-banner-sdk th,#onetrust-banner-sdk td,#onetrust-pc-sdk th,#onetrust-pc-sdk td,#ot-sdk-cookie-policy th,#ot-sdk-cookie-policy td{padding:12px 15px;text-align:left;border-bottom:1px solid #e1e1e1}#onetrust-banner-sdk button,#onetrust-pc-sdk button,#ot-sdk-cookie-policy button{margin-bottom:1rem;font-family:inherit}#onetrust-banner-sdk .ot-sdk-container:after,#onetrust-banner-sdk .ot-sdk-row:after,#onetrust-pc-sdk .ot-sdk-container:after,#onetrust-pc-sdk .ot-sdk-row:after,#ot-sdk-cookie-policy .ot-sdk-container:after,#ot-sdk-cookie-policy .ot-sdk-row:after{content:"";display:table;clear:both}#onetrust-banner-sdk .ot-sdk-row,#onetrust-pc-sdk .ot-sdk-row,#ot-sdk-cookie-policy .ot-sdk-row{margin:0;max-width:none;display:block}
.ot-sdk-cookie-policy{font-family:inherit;font-size:16px}.ot-sdk-cookie-policy.otRelFont{font-size:1rem}.ot-sdk-cookie-policy h3,.ot-sdk-cookie-policy h4,.ot-sdk-cookie-policy h6,.ot-sdk-cookie-policy p,.ot-sdk-cookie-policy li,.ot-sdk-cookie-policy a,.ot-sdk-cookie-policy th,.ot-sdk-cookie-policy #cookie-policy-description,.ot-sdk-cookie-policy .ot-sdk-cookie-policy-group,.ot-sdk-cookie-policy #cookie-policy-title{color:dimgray}.ot-sdk-cookie-policy #cookie-policy-description{margin-bottom:1em}.ot-sdk-cookie-policy h4{font-size:1.2em}.ot-sdk-cookie-policy h6{font-size:1em;margin-top:2em}.ot-sdk-cookie-policy th{min-width:75px}.ot-sdk-cookie-policy a,.ot-sdk-cookie-policy a:hover{background:#fff}.ot-sdk-cookie-policy thead{background-color:#f6f6f4;font-weight:bold}.ot-sdk-cookie-policy .ot-mobile-border{display:none}.ot-sdk-cookie-policy section{margin-bottom:2em}.ot-sdk-cookie-policy table{border-collapse:inherit}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy{font-family:inherit;font-size:1rem}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy h3,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy h4,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy h6,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy p,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy li,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy a,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy th,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy #cookie-policy-description,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy .ot-sdk-cookie-policy-group,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy #cookie-policy-title{color:dimgray}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy #cookie-policy-description{margin-bottom:1em}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy .ot-sdk-subgroup{margin-left:1.5em}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy #cookie-policy-description,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy .ot-sdk-cookie-policy-group-desc,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy .ot-table-header,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy a,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy span,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy td{font-size:.9em}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy td span,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy td a{font-size:inherit}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy .ot-sdk-cookie-policy-group{font-size:1em;margin-bottom:.6em}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy .ot-sdk-cookie-policy-title{margin-bottom:1.2em}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy&gt;section{margin-bottom:1em}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy th{min-width:75px}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy a,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy a:hover{background:#fff}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy thead{background-color:#f6f6f4;font-weight:bold}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy .ot-mobile-border{display:none}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy section{margin-bottom:2em}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy .ot-sdk-subgroup ul li{list-style:disc;margin-left:1.5em}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy .ot-sdk-subgroup ul li h4{display:inline-block}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table{border-collapse:inherit;margin:auto;border:1px solid #d7d7d7;border-radius:5px;border-spacing:initial;width:100%;overflow:hidden}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table th,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table td{border-bottom:1px solid #d7d7d7;border-right:1px solid #d7d7d7}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table tr:last-child td{border-bottom:0px}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table tr th:last-child,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table tr td:last-child{border-right:0px}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table .ot-host,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table .ot-cookies-type{width:25%}.ot-sdk-cookie-policy[dir=rtl]{text-align:left}#ot-sdk-cookie-policy h3{font-size:1.5em}@media only screen and (max-width: 530px){.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) table,.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) thead,.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) tbody,.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) th,.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) td,.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) tr{display:block}.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) thead tr{position:absolute;top:-9999px;left:-9999px}.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) tr{margin:0 0 1em 0}.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) tr:nth-child(odd),.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) tr:nth-child(odd) a{background:#f6f6f4}.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) td{border:none;border-bottom:1px solid #eee;position:relative;padding-left:50%}.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) td:before{position:absolute;height:100%;left:6px;width:40%;padding-right:10px}.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) .ot-mobile-border{display:inline-block;background-color:#e4e4e4;position:absolute;height:100%;top:0;left:45%;width:2px}.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) td:before{content:attr(data-label);font-weight:bold}.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) li{word-break:break-word;word-wrap:break-word}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table{overflow:hidden}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table td{border:none;border-bottom:1px solid #d7d7d7}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy thead,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy tbody,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy th,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy td,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy tr{display:block}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table .ot-host,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table .ot-cookies-type{width:auto}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy tr{margin:0 0 1em 0}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy td:before{height:100%;width:40%;padding-right:10px}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy td:before{content:attr(data-label);font-weight:bold}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy li{word-break:break-word;word-wrap:break-word}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy thead tr{position:absolute;top:-9999px;left:-9999px;z-index:-9999}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table tr:last-child td{border-bottom:1px solid #d7d7d7;border-right:0px}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table tr:last-child td:last-child{border-bottom:0px}}

                    #ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy h5,
                    #ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy h6,
                    #ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy li,
                    #ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy p,
                    #ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy a,
                    #ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy span,
                    #ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy td,
                    #ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy #cookie-policy-description {
                        color: #696969;
                    }
                    #ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy th {
                        color: #696969;
                    }
                    #ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy .ot-sdk-cookie-policy-group {
                        color: #696969;
                    }

                    #ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy #cookie-policy-title {
                            color: #696969;
                        }


                    #ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table th {
                            background-color: #F8F8F8;
                        }

            .ot-floating-button__front{background-image:url('https://cdn.cookielaw.org/logos/static/ot_persistent_cookie.png')}</div></head>
    <body class="question-page unified-theme">
    <div id="notify-container"></div>
    <div id="custom-header"></div>

<header class="s-topbar ps-fixed t0 l0 js-top-bar">
    <div class="s-topbar--container">
            <a href="#" class="s-topbar--menu-btn js-left-sidebar-toggle" role="menuitem" aria-haspopup="true" aria-controls="left-sidebar" aria-expanded="false"><span></span></a>
            <div class="topbar-dialog leftnav-dialog js-leftnav-dialog dno">
                <div class="left-sidebar js-unpinned-left-sidebar" data-is-here-when="sm" id="left-sidebar">
    <div class="left-sidebar--sticky-container js-sticky-leftnav">
        <nav role="navigation">
            <ol class="nav-links">


<li class="ps-relative">


    <a href="/" class="pl8 js-gps-track nav-links--link" data-gps-track="top_nav.click({is_current: false, location:2, destination:8})" aria-controls="" data-controller="" data-s-popover-placement="right" data-s-popover-auto-show="true" data-s-popover-hide-on-outside-click="never">
            <div class="d-flex ai-center">
                <div class="flex--item truncate">
                    Home
                </div>
            </div>
    </a>
</li>

                <li>
                    <ol class="nav-links">
                            <li class="fs-fine tt-uppercase ml8 mt16 mb4 fc-light">Public</li>



<li class="ps-relative  youarehere">


    <a id="nav-questions" href="/questions" class="pl8 js-gps-track nav-links--link -link__with-icon" data-gps-track="top_nav.click({is_current: true, location:2, destination:1})" aria-controls="" data-controller="" data-s-popover-placement="right" data-s-popover-auto-show="true" data-s-popover-hide-on-outside-click="never">
<svg aria-hidden="true" class="svg-icon iconGlobe" width="18" height="18" viewBox="0 0 18 18"><path d="M9 1C4.64 1 1 4.64 1 9c0 4.36 3.64 8 8 8 4.36 0 8-3.64 8-8 0-4.36-3.64-8-8-8ZM8 15.32a6.46 6.46 0 0 1-4.3-2.74 6.46 6.46 0 0 1-.93-5.01L7 11.68v.8c0 .88.12 1.32 1 1.32v1.52Zm5.72-2c-.2-.66-1-1.32-1.72-1.32h-1v-2c0-.44-.56-1-1-1H6V7h1c.44 0 1-.56 1-1V5h2c.88 0 1.4-.72 1.4-1.6v-.33a6.45 6.45 0 0 1 3.83 4.51 6.45 6.45 0 0 1-1.51 5.73v.01Z"></path></svg>            <span class="-link--channel-name">Questions</span>
    </a>
</li>



<li class="ps-relative">


    <a id="nav-tags" href="/tags" class=" js-gps-track nav-links--link" data-gps-track="top_nav.click({is_current: false, location:2, destination:2})" aria-controls="" data-controller="" data-s-popover-placement="right" data-s-popover-auto-show="true" data-s-popover-hide-on-outside-click="never">
            <div class="d-flex ai-center">
                <div class="flex--item truncate">
                    Tags
                </div>
            </div>
    </a>
</li>



<li class="ps-relative">


    <a id="nav-users" href="/users" class=" js-gps-track nav-links--link" data-gps-track="top_nav.click({is_current: false, location:2, destination:3})" aria-controls="" data-controller="" data-s-popover-placement="right" data-s-popover-auto-show="true" data-s-popover-hide-on-outside-click="never">
            <div class="d-flex ai-center">
                <div class="flex--item truncate">
                    Users
                </div>
            </div>
    </a>
</li>



<li class="ps-relative">


    <a id="nav-companies" href="https://stackoverflow.com/jobs/companies?so_medium=stackoverflow&amp;so_source=SiteNav" class=" js-gps-track nav-links--link" data-gps-track="top_nav.click({is_current: false, location:2, destination:12})" aria-controls="" data-controller="" data-s-popover-placement="right" data-s-popover-auto-show="true" data-s-popover-hide-on-outside-click="never">
            <div class="d-flex ai-center">
                <div class="flex--item truncate">
                    Companies
                </div>
            </div>
    </a>
</li>

                                <li class="d-flex ml8 mt16 jc-space-between">
                                    <div class="flex--item tt-uppercase tt-uppercase fs-fine fc-light">Collectives</div>
                                    <div class="flex--item fs-fine fc-light">
                                        <a href="javascript:void(0)" class="s-link s-link__inherit mr8 js-gps-track js-collectives-navcta-toggle" role="button" aria-controls="popover-discover-collectives" data-controller="s-popover" data-action="s-popover#toggle" data-s-popover-placement="top" data-s-popover-toggle-class="is-selected" data-gps-track="top_nav.click({is_current:false, location:2, destination:17})" aria-expanded="false">
                                            <svg aria-hidden="true" class="svg-icon iconInfoSm" width="14" height="14" viewBox="0 0 14 14"><path d="M7 1a6 6 0 1 1 0 12A6 6 0 0 1 7 1Zm1 10V6H6v5h2Zm0-6V3H6v2h2Z"></path></svg>
                                        </a>
                                    </div>
                                </li>


<li class="ps-relative">


    <a id="nav-collective-discover" href="/collectives" class="pl8 ai-center js-collectives-navcta-toggle js-gps-track nav-links--link -link__with-icon" data-gps-track="top_nav.click({is_current: false, location:2, destination:18})" aria-controls="" data-controller="" data-s-popover-placement="right" data-s-popover-auto-show="true" data-s-popover-hide-on-outside-click="never">
<svg aria-hidden="true" class="mt-auto fc-orange-400 svg-icon iconStarVerified" width="18" height="18" viewBox="0 0 18 18"><path d="M9.86.89a1.14 1.14 0 0 0-1.72 0l-.5.58c-.3.35-.79.48-1.23.33l-.72-.25a1.14 1.14 0 0 0-1.49.85l-.14.76c-.1.45-.45.8-.9.9l-.76.14c-.67.14-1.08.83-.85 1.49l.25.72c.15.44.02.92-.33 1.23l-.58.5a1.14 1.14 0 0 0 0 1.72l.58.5c.35.3.48.79.33 1.23l-.25.72c-.23.66.18 1.35.85 1.49l.76.14c.45.1.8.45.9.9l.14.76c.14.67.83 1.08 1.49.85l.72-.25c.44-.15.92-.02 1.23.33l.5.58c.46.52 1.26.52 1.72 0l.5-.58c.3-.35.79-.48 1.23-.33l.72.25c.66.23 1.35-.18 1.49-.85l.14-.76c.1-.45.45-.8.9-.9l.76-.14c.67-.14 1.08-.83.85-1.49l-.25-.72c-.15-.44-.02-.92.33-1.23l.58-.5c.52-.46.52-1.26 0-1.72l-.58-.5c-.35-.3-.48-.79-.33-1.23l.25-.72a1.14 1.14 0 0 0-.85-1.49l-.76-.14c-.45-.1-.8-.45-.9-.9l-.14-.76a1.14 1.14 0 0 0-1.49-.85l-.72.25c-.44.15-.92.02-1.23-.33l-.5-.58Zm-.49 2.67L10.6 6.6c.05.15.19.24.34.25l3.26.22c.36.03.5.48.23.71l-2.5 2.1a.4.4 0 0 0-.14.4l.8 3.16a.4.4 0 0 1-.6.44L9.2 12.13a.4.4 0 0 0-.42 0l-2.77 1.74a.4.4 0 0 1-.6-.44l.8-3.16a.4.4 0 0 0-.13-.4l-2.5-2.1a.4.4 0 0 1 .22-.7l3.26-.23a.4.4 0 0 0 .34-.25l1.22-3.03a.4.4 0 0 1 .74 0Z"></path></svg>            <span class="-link--channel-name">Explore Collectives</span>
    </a>
</li>

                    </ol>
                </li>



<li>
    <ol class="nav-links">


<div class="js-freemium-cta ps-relative">

    <div class="fs-fine tt-uppercase ml8 mt16 mb8 fc-light">Teams</div>

    <div class="bt bl bb bc-black-075 p12 pb6 fc-black-600 blr-sm overflow-hidden">
        <strong class="fc-black-750 mb6">Stack Overflow for Teams</strong>
        – Start collaborating and sharing organizational knowledge.

        <img class="wmx100 mx-auto my8 h-auto d-block" width="139" height="114" src="https://cdn.sstatic.net/Img/teams/teams-illo-free-sidebar-promo.svg?v=47faa659a05e" alt="">

        <a href="https://try.stackoverflow.co/why-teams/?utm_source=so-owned&amp;utm_medium=side-bar&amp;utm_campaign=campaign-38&amp;utm_content=cta" class="w100 s-btn s-btn__primary s-btn__xs bg-orange-400 js-gps-track" data-gps-track="teams.create.left-sidenav.click({ Action: 6 })" data-ga="[&quot;teams left navigation - anonymous&quot;,&quot;left nav free cta&quot;,&quot;stackoverflow.com/teams/create/free&quot;,null,null]">Create a free Team</a>
        <a href="https://stackoverflow.co/teams" class="w100 s-btn s-btn__muted s-btn__xs js-gps-track" data-gps-track="teams.create.left-sidenav.click({ Action: 5 })" data-ga="[&quot;teams left navigation - anonymous&quot;,&quot;left nav free cta&quot;,&quot;stackoverflow.com/teams&quot;,null,null]">Why Teams?</a>

    </div>
</div>

            <li class="d-flex ai-center jc-space-between ml8 mt24 mb4 js-create-team-cta d-none">
                <div class="flex--item tt-uppercase fs-fine fc-light">Teams</div>
                <div class="flex--item">
                    <a href="javascript:void(0)" class="s-link p12 fc-black-500 h:fc-black-800 js-gps-track" role="button" aria-controls="popover-teams-create-cta" data-controller="s-popover" data-action="s-popover#toggle" data-s-popover-placement="bottom-start" data-s-popover-toggle-class="is-selected" data-gps-track="teams.create.left-sidenav.click({ Action: ShowInfo })" data-ga="[&quot;teams left navigation - anonymous&quot;,&quot;left nav show teams info&quot;,null,null,null]" aria-expanded="false">
                        <svg aria-hidden="true" class="svg-icon iconInfoSm" width="14" height="14" viewBox="0 0 14 14"><path d="M7 1a6 6 0 1 1 0 12A6 6 0 0 1 7 1Zm1 10V6H6v5h2Zm0-6V3H6v2h2Z"></path></svg>
                    </a>

                </div>
            </li>
            <li class="ps-relative js-create-team-cta d-none">
                <a href="https://stackoverflow.com/teams/create/free?utm_source=so-owned&amp;utm_medium=side-bar&amp;utm_campaign=campaign-38&amp;utm_content=cta" class="pl8 js-gps-track nav-links--link" title="Stack Overflow for Teams is a private, secure spot for your organization's questions and answers." data-gps-track="teams.create.left-sidenav.click({ Action: FreemiumTeamsCreateClick })" data-ga="[&quot;teams left navigation - anonymous&quot;,&quot;left nav team click&quot;,&quot;stackoverflow.com/teams/create/free&quot;,null,null]">
                    <div class="d-flex ai-center">
                        <div class="flex--item s-avatar va-middle bg-orange-400">
                            <div class="s-avatar--letter mtn1">
                                <svg aria-hidden="true" class="svg-icon iconBriefcaseSm" width="14" height="14" viewBox="0 0 14 14"><path d="M4 3a1 1 0 0 1 1-1h4a1 1 0 0 1 1 1v1h.5c.83 0 1.5.67 1.5 1.5v5c0 .83-.67 1.5-1.5 1.5h-7A1.5 1.5 0 0 1 2 10.5v-5C2 4.67 2.67 4 3.5 4H4V3Zm5 1V3H5v1h4Z"></path></svg>
                            </div>
                            <svg aria-hidden="true" class="native s-avatar--badge svg-icon iconShieldXSm" width="9" height="10" viewBox="0 0 9 10"><path d="M0 1.84 4.5 0 9 1.84v3.17C9 7.53 6.3 10 4.5 10 2.7 10 0 7.53 0 5.01V1.84Z" fill="var(--white)"></path><path d="M1 2.5 4.5 1 8 2.5v2.51C8 7.34 5.34 9 4.5 9 3.65 9 1 7.34 1 5.01V2.5Zm2.98 3.02L3.2 7h2.6l-.78-1.48a.4.4 0 0 1 .15-.38c.34-.24.73-.7.73-1.14 0-.71-.5-1.23-1.41-1.23-.92 0-1.39.52-1.39 1.23 0 .44.4.9.73 1.14.12.08.18.23.15.38Z" fill="var(--black-500)"></path></svg>
                        </div>
                        <div class="flex--item pl6">
                            Create free Team
                        </div>
                    </div>
                </a>
            </li>
    </ol>
</li>
            </ol>
        </nav>
    </div>

        <div class="s-popover ws2" id="popover-discover-collectives" role="menu">
            <div class="s-popover--arrow"></div>
            <div>
                <svg aria-hidden="true" class="fc-orange-500 float-right ml24 svg-spot spotCollective" width="48" height="48" viewBox="0 0 48 48"><path d="M25.5 7a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5ZM14 18.25c0-.69.56-1.25 1.25-1.25h22.5c.69 0 1.25.56 1.25 1.25V37.5a1 1 0 0 1-1.6.8l-4.07-3.05a1.25 1.25 0 0 0-.75-.25H15.25c-.69 0-1.25-.56-1.25-1.25v-15.5ZM7 24.5a2.5 2.5 0 1 1-5 0 2.5 2.5 0 0 1 5 0ZM25.5 48a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5ZM48 24.5a2.5 2.5 0 1 1-5 0 2.5 2.5 0 0 1 5 0Z" opacity=".2"></path><path d="M21 3.5a3.5 3.5 0 1 1 7 0 3.5 3.5 0 0 1-7 0ZM24.5 2a1.5 1.5 0 1 0 0 3 1.5 1.5 0 0 0 0-3ZM0 23.5a3.5 3.5 0 1 1 7 0 3.5 3.5 0 0 1-7 0ZM3.5 22a1.5 1.5 0 1 0 0 3 1.5 1.5 0 0 0 0-3ZM21 44.5a3.5 3.5 0 1 1 7 0 3.5 3.5 0 0 1-7 0Zm3.5-1.5a1.5 1.5 0 1 0 0 3 1.5 1.5 0 0 0 0-3Zm20-23a3.5 3.5 0 1 0 0 7 3.5 3.5 0 0 0 0-7ZM43 23.5a1.5 1.5 0 1 1 3 0 1.5 1.5 0 0 1-3 0Zm-23.23-3.14a1 1 0 0 1-.13 1.4l-2.08 1.74 2.08 1.73a1 1 0 1 1-1.28 1.54l-2.42-2.02a1.63 1.63 0 0 1 0-2.5l2.42-2.02a1 1 0 0 1 1.4.13Zm7.59 1.41a1 1 0 1 1 1.28-1.54l2.42 2.02c.78.65.78 1.85 0 2.5l-2.42 2.02a1 1 0 1 1-1.28-1.54l2.08-1.73-2.08-1.73ZM24.12 18a1 1 0 0 1 .87 1.12l-1 8a1 1 0 1 1-1.98-.24l1-8a1 1 0 0 1 1.11-.87Zm-11.87-5C11.01 13 10 14 10 15.25v15.5c0 1.24 1 2.25 2.25 2.25h17.33c.06 0 .11.02.15.05l4.07 3.05a2 2 0 0 0 3.2-1.6V15.25c0-1.24-1-2.25-2.25-2.25h-22.5ZM12 15.25c0-.14.11-.25.25-.25h22.5c.14 0 .25.11.25.25V34.5l-4.07-3.05a2.2 2.2 0 0 0-1.35-.45H12.25a.25.25 0 0 1-.25-.25v-15.5Zm7.24-10.68a1 1 0 1 0-.48-1.94A22.04 22.04 0 0 0 2.91 17.7a1 1 0 1 0 1.92.58 20.04 20.04 0 0 1 14.4-13.72Zm11.05-1.66a1 1 0 0 0-.58 1.92c6.45 1.92 11.54 7 13.46 13.46a1 1 0 1 0 1.92-.58 22.05 22.05 0 0 0-14.8-14.8ZM4.57 28.76a1 1 0 0 0-1.94.48 22.03 22.03 0 0 0 16.13 16.13 1 1 0 1 0 .48-1.94A20.03 20.03 0 0 1 4.57 28.76Zm40.8.48a1 1 0 1 0-1.94-.48 20.04 20.04 0 0 1-13.72 14.41 1 1 0 0 0 .58 1.92 22.04 22.04 0 0 0 15.08-15.85Z"></path></svg>
                <div class="pt4 fw-bold">Collectives™ on Stack Overflow</div>
                <p class="my16 fs-caption fc-medium">Find centralized, trusted content and collaborate around the technologies you use most.</p>
                <a href="/collectives" class="js-gps-track s-btn s-btn__primary s-btn__xs" data-gps-track="top_nav.click({is_current:false, location:2, destination:18})">
                    Learn more
                </a>
            </div>
        </div>


        <div class="s-popover" id="popover-teams-create-cta" role="menu" aria-hidden="true">
            <div class="s-popover--arrow"></div>

            <div class="ps-relative overflow-hidden">
                <p class="mb2"><strong>Teams</strong></p>
                <p class="mb12 fs-caption fc-black-400">Q&amp;A for work</p>
                <p class="mb12 fs-caption fc-medium">Connect and share knowledge within a single location that is structured and easy to search.</p>
                <a href="https://stackoverflow.co/teams" class="js-gps-track s-btn s-btn__primary s-btn__xs" data-gps-track="teams.create.left-sidenav.click({ Action: CtaClick })" data-ga="[&quot;teams left navigation - anonymous&quot;,&quot;left nav cta&quot;,&quot;stackoverflow.com/teams&quot;,null,null]">
                    Learn more
                </a>
            </div>

            <div class="ps-absolute t8 r8">
                <svg aria-hidden="true" class="fc-orange-500 svg-spot spotPeople" width="48" height="48" viewBox="0 0 48 48"><path d="M13.5 28a4.5 4.5 0 1 0 0-9 4.5 4.5 0 0 0 0 9ZM7 30a1 1 0 0 1 1-1h11a1 1 0 0 1 1 1v5h11v-5a1 1 0 0 1 1-1h12a1 1 0 0 1 1 1v10a2 2 0 0 1-2 2H33v5a1 1 0 0 1-1 1H20a1 1 0 0 1-1-1v-5H8a1 1 0 0 1-1-1V30Zm25-6.5a4.5 4.5 0 1 0 9 0 4.5 4.5 0 0 0-9 0ZM24.5 34a4.5 4.5 0 1 0 0-9 4.5 4.5 0 0 0 0 9Z" opacity=".2"></path><path d="M16.4 26.08A6 6 0 1 0 7.53 26C5.64 26.06 4 27.52 4 29.45V40a1 1 0 0 0 1 1h9a1 1 0 1 0 0-2h-4v-7a1 1 0 1 0-2 0v7H6v-9.55c0-.73.67-1.45 1.64-1.45H16a1 1 0 0 0 .4-1.92ZM12 18a4 4 0 1 1 0 8 4 4 0 0 1 0-8Zm16.47 14a6 6 0 1 0-8.94 0A3.6 3.6 0 0 0 16 35.5V46a1 1 0 0 0 1 1h14a1 1 0 0 0 1-1V35.5c0-1.94-1.64-3.42-3.53-3.5ZM20 28a4 4 0 1 1 8 0 4 4 0 0 1-8 0Zm-.3 6h8.6c1 0 1.7.75 1.7 1.5V45h-2v-7a1 1 0 1 0-2 0v7h-4v-7a1 1 0 1 0-2 0v7h-2v-9.5c0-.75.7-1.5 1.7-1.5ZM42 22c0 1.54-.58 2.94-1.53 4A3.5 3.5 0 0 1 44 29.45V40a1 1 0 0 1-1 1h-9a1 1 0 1 1 0-2h4v-7a1 1 0 1 1 2 0v7h2v-9.55A1.5 1.5 0 0 0 40.48 28H32a1 1 0 0 1-.4-1.92A6 6 0 1 1 42 22Zm-2 0a4 4 0 1 0-8 0 4 4 0 0 0 8 0Z"></path><g opacity=".35"><path d="M17 10a1 1 0 011-1h12a1 1 0 110 2H18a1 1 0 01-1-1Zm1-5a1 1 0 100 2h12a1 1 0 100-2H18ZM14 1a1 1 0 00-1 1v12a1 1 0 001 1h5.09l4.2 4.2a1 1 0 001.46-.04l3.7-4.16H34a1 1 0 001-1V2a1 1 0 00-1-1H14Zm1 12V3h18v10h-5a1 1 0 00-.75.34l-3.3 3.7-3.74-3.75a1 1 0 00-.71-.29H15Z"></path></g></svg>
            </div>
        </div>


</div>
            </div>
                <a href="https://stackoverflow.com" class="s-topbar--logo js-gps-track" data-gps-track="top_nav.click({is_current:false, location:2, destination:8})">
                    <span class="-img _glyph">Stack Overflow</span>
                </a>



            <ol class="s-navigation" role="presentation">

                    <li class="md:d-none">
                        <a href="https://stackoverflow.co/" class="s-navigation--item js-gps-track" data-gps-track="top_nav.products.click({location:2, destination:7})" data-ga="[&quot;top navigation&quot;,&quot;about menu click&quot;,null,null,null]">About</a>
                    </li>

                <li>
                    <a href="#" class="s-navigation--item js-gps-track js-products-menu" aria-controls="products-popover" data-controller="s-popover" data-action="s-popover#toggle" data-s-popover-placement="bottom" data-s-popover-toggle-class="is-selected" data-gps-track="top_nav.products.click({location:2, destination:1})" data-ga="[&quot;top navigation&quot;,&quot;products menu click&quot;,null,null,null]" aria-expanded="false">
                        Products
                    </a>
                </li>

                    <li class="md:d-none">
                        <a href="/teams" class="s-navigation--item js-gps-track" data-gps-track="top_nav.products.click({location:2, destination:7})" data-ga="[&quot;top navigation&quot;,&quot;learn more - teams&quot;,null,null,null]">For Teams</a>
                    </li>
            </ol>
            <div class="s-popover ws2 mtn2 p0" id="products-popover" role="menu" aria-hidden="true">
                <div class="s-popover--arrow"></div>
                <ol class="list-reset s-anchors s-anchors__inherit">
                    <li class="m6">
                        <a href="/questions" class="bar-sm p6 d-block h:bg-black-100 js-gps-track" data-gps-track="top_nav.products.click({location:2, destination:2})" data-ga="[&quot;top navigation&quot;,&quot;public qa submenu click&quot;,null,null,null]">
                            <span class="fs-body1 d-block">Stack Overflow</span>
                            <span class="fs-caption d-block fc-light">Public questions &amp; answers</span>
                        </a>
                    </li>
                    <li class="m6">
                        <a href="/teams" class="bar-sm p6 d-block h:bg-black-100 js-gps-track" data-gps-track="top_nav.products.click({location:2, destination:3})" data-ga="[&quot;top navigation&quot;,&quot;teams submenu click&quot;,null,null,null]">
                            <span class="fs-body1 d-block">Stack Overflow for Teams</span>
                            <span class="fs-caption d-block fc-light">Where developers &amp; technologists share private knowledge with coworkers</span>
                        </a>
                    </li>
                    <li class="m6">
                        <a href="https://stackoverflow.co/talent" class="bar-sm p6 d-block h:bg-black-100 js-gps-track" data-gps-track="top_nav.products.click({location:2, destination:5})" data-ga="[&quot;top navigation&quot;,&quot;talent submenu click&quot;,null,null,null]">
                            <span class="fs-body1 d-block">Talent</span>
                            <span class="fs-caption d-block fc-light">
                                Build your employer brand
                            </span>
                        </a>
                    </li>
                    <li class="m6">
                        <a href="https://stackoverflow.co/advertising" class="bar-sm p6 d-block h:bg-black-100 js-gps-track" data-gps-track="top_nav.products.click({location:2, destination:6})" data-ga="[&quot;top navigation&quot;,&quot;advertising submenu click&quot;,null,null,null]">
                            <span class="fs-body1 d-block">Advertising</span>
                            <span class="fs-caption d-block fc-light">Reach developers &amp; technologists worldwide</span>
                        </a>
                    </li>
                    <li class="bg-black-025 bt bc-black-075 py6 px6 bbr-md">
                        <a href="https://stackoverflow.co/" class="fc-light d-block py6 px6 h:fc-black-800 js-gps-track" data-gps-track="top_nav.products.click({location:2, destination:7})" data-ga="[&quot;top navigation&quot;,&quot;about submenu click&quot;,null,null,null]">About the company</a>
                    </li>
                </ol>
            </div>

            <form id="search" role="search" action="/search" class="s-topbar--searchbar js-searchbar " autocomplete="off">
                    <div class="s-topbar--searchbar--input-group">
                        <input name="q" type="text" placeholder="Search…" value="" autocomplete="off" maxlength="240" class="s-input s-input__search js-search-field " aria-label="Search" aria-controls="top-search" data-controller="s-popover" data-action="focus->s-popover#show" data-s-popover-placement="bottom-start" aria-expanded="false">
                        <svg aria-hidden="true" class="s-input-icon s-input-icon__search svg-icon iconSearch" width="18" height="18" viewBox="0 0 18 18"><path d="m18 16.5-5.14-5.18h-.35a7 7 0 1 0-1.19 1.19v.35L16.5 18l1.5-1.5ZM12 7A5 5 0 1 1 2 7a5 5 0 0 1 10 0Z"></path></svg>
                        <div class="s-popover p0 wmx100 wmn4 sm:wmn-initial js-top-search-popover" id="top-search" role="menu">
    <div class="s-popover--arrow"></div>
    <div class="js-spinner p24 d-flex ai-center jc-center d-none">
        <div class="s-spinner s-spinner__sm fc-orange-400">
            <div class="v-visible-sr">Loading…</div>
        </div>
    </div>

    <span class="v-visible-sr js-screen-reader-info"></span>
    <div class="js-ac-results overflow-y-auto hmx3 d-none"></div>

    <div class="js-search-hints" aria-describedby="Tips for searching"></div>
</div>
                    </div>
            </form>



<ol class="s-topbar--content" role="presentation">



    <li class="js-topbar-dialog-corral" role="presentation">


    <div class="topbar-dialog siteSwitcher-dialog dno" role="menu">
        <div class="header fw-wrap">
            <h3 class="flex--item">
                <a href="https://stackoverflow.com">current community</a>
            </h3>
            <div class="flex--item fl1">
                <div class="ai-center d-flex jc-end">
                    <button class="js-close-button s-btn s-btn__muted p0 ml8 d-none sm:d-block" type="button" aria-label="Close">
                        <svg aria-hidden="true" class="svg-icon iconClear" width="18" height="18" viewBox="0 0 18 18"><path d="M15 4.41 13.59 3 9 7.59 4.41 3 3 4.41 7.59 9 3 13.59 4.41 15 9 10.41 13.59 15 15 13.59 10.41 9 15 4.41Z"></path></svg>
                    </button>
                </div>
            </div>
        </div>
        <div class="modal-content bg-powder-050 current-site-container">
            <ul class="current-site ">
                    <li class="d-flex">
                            <div class="fl1">
                <a href="https://stackoverflow.com" class="current-site-link site-link js-gps-track d-flex gs8 gsx" data-id="1" data-gps-track="site_switcher.click({ item_type:3 })">
        <div class="favicon favicon-stackoverflow site-icon flex--item" title="Stack Overflow"></div>
        <span class="flex--item fl1">
            Stack Overflow
        </span>
    </a>

    </div>
    <div class="related-links">
            <a href="https://stackoverflow.com/help" class="js-gps-track" data-gps-track="site_switcher.click({ item_type:14 })">help</a>
            <a href="https://chat.stackoverflow.com/?tab=site&amp;host=stackoverflow.com" class="js-gps-track" data-gps-track="site_switcher.click({ item_type:6 })">chat</a>
    </div>

                    </li>
                    <li class="related-site d-flex">
                            <div class="L-shaped-icon-container">
        <span class="L-shaped-icon"></span>
    </div>

                            <a href="https://meta.stackoverflow.com" class=" site-link js-gps-track d-flex gs8 gsx" data-id="552" data-gps-track="site.switch({ target_site:552, item_type:3 }),site_switcher.click({ item_type:4 })">
        <div class="favicon favicon-stackoverflowmeta site-icon flex--item" title="Meta Stack Overflow"></div>
        <span class="flex--item fl1">
            Meta Stack Overflow
        </span>
    </a>

                    </li>
            </ul>
        </div>

        <div class="header" id="your-communities-header">
            <h3>
your communities            </h3>

        </div>
        <div class="modal-content" id="your-communities-section">

                <div class="call-to-login">
<a href="https://stackoverflow.com/users/signup?ssrc=site_switcher&amp;returnurl=https%3a%2f%2fstackoverflow.com%2fquestions%2f73013700%2fhow-can-i-get-my-django-server-to-reload-when-i-change-the-html-in-dev-mode-with%2f73013747" class="login-link js-gps-track" data-gps-track="site_switcher.click({ item_type:10 })">Sign up</a> or <a href="https://stackoverflow.com/users/login?ssrc=site_switcher&amp;returnurl=https%3a%2f%2fstackoverflow.com%2fquestions%2f73013700%2fhow-can-i-get-my-django-server-to-reload-when-i-change-the-html-in-dev-mode-with%2f73013747" class="login-link js-gps-track" data-gps-track="site_switcher.click({ item_type:11 })">log in</a> to customize your list.                </div>
        </div>

        <div class="header">
            <h3><a href="https://stackexchange.com/sites">more stack exchange communities</a>
            </h3>
            <a href="https://stackoverflow.blog" class="float-right">company blog</a>
        </div>
        <div class="modal-content">
                <div class="child-content"></div>
        </div>
    </div>

    </li>

            <li><a href="#" class="s-topbar--item s-btn s-btn__icon s-btn__muted d-none sm:d-inline-flex js-searchbar-trigger" role="button" aria-label="Search" aria-haspopup="true" aria-controls="search" title="Click to show search"><svg aria-hidden="true" class="svg-icon iconSearch" width="18" height="18" viewBox="0 0 18 18"><path d="m18 16.5-5.14-5.18h-.35a7 7 0 1 0-1.19 1.19v.35L16.5 18l1.5-1.5ZM12 7A5 5 0 1 1 2 7a5 5 0 0 1 10 0Z"></path></svg></a></li>
                    <li>
                        <a href="https://stackoverflow.com/users/login?ssrc=head&amp;returnurl=https%3a%2f%2fstackoverflow.com%2fquestions%2f73013700%2fhow-can-i-get-my-django-server-to-reload-when-i-change-the-html-in-dev-mode-with%2f73013747" class="s-topbar--item s-topbar--item__unset s-btn s-btn__filled ws-nowrap js-gps-track" rel="nofollow" data-gps-track="login.click" data-ga="[&quot;top navigation&quot;,&quot;login button click&quot;,null,null,null]">Log in</a>
                    </li>
                    <li><a href="https://stackoverflow.com/users/signup?ssrc=head&amp;returnurl=https%3a%2f%2fstackoverflow.com%2fquestions%2f73013700%2fhow-can-i-get-my-django-server-to-reload-when-i-change-the-html-in-dev-mode-with%2f73013747" class="s-topbar--item s-topbar--item__unset ml4 s-btn s-btn__primary ws-nowrap" rel="nofollow" data-ga="[&quot;sign up&quot;,&quot;Sign Up Navigation&quot;,&quot;Header&quot;,null,null]">Reload</a></li>
</ol>


    </div>
</header>

    <script>
        StackExchange.ready(function () { StackExchange.topbar.init(); });
        StackExchange.scrollPadding.setPaddingTop(50, 10);
    </script>





    <div class="container">


<div data-is-here-when="md lg" class="left-sidebar js-pinned-left-sidebar ps-relative" data-can-be="left-sidebar"></div>




        <div id="content" class="snippet-hidden">



<div itemprop="mainEntity" itemscope="" itemtype="https://schema.org/Question">
    <link itemprop="image" href="https://cdn.sstatic.net/Sites/stackoverflow/Img/apple-touch-icon.png?v=c78bd457575a">

    <div class="inner-content clearfix">



            <div id="question-header" class="d-flex sm:fd-column">
                        <h1 itemprop="name" class="fs-headline1 ow-break-word mb8 flex--item fl1"><a href="/questions/73013700/how-can-i-get-my-django-server-to-reload-when-i-change-the-html-in-dev-mode-with" class="question-hyperlink">How can I get my Django server to reload when I change the HTML in dev mode without clicking the refresh button?</a></h1>
                <div class="ml12 aside-cta flex--item print:d-none sm:ml0 sm:mb12 sm:order-first sm:as-end">
                        <a href="/questions/ask" class="ws-nowrap s-btn s-btn__primary">
        Ask Question
    </a>

                </div>
            </div>
            <div class="d-flex fw-wrap pb8 mb16 bb bc-black-075">
                    <div class="flex--item ws-nowrap mr16 mb8" title="2022-07-17 16:53:28Z">
                        <span class="fc-light mr2">Asked</span>
                        <time itemprop="dateCreated" datetime="2022-07-17T16:53:28">today</time>
                    </div>
                    <div class="flex--item ws-nowrap mr16 mb8">
                        <span class="fc-light mr2">Modified</span>
                        <a href="?lastactivity" class="s-link s-link__inherit" title="2022-07-17 17:00:23Z">today</a>
                    </div>
                    <div class="flex--item ws-nowrap mb8" title="Viewed 11 times">
                        <span class="fc-light mr2">Viewed</span>
                        11 times
                    </div>
            </div>
            <div id="mainbar" role="main" aria-label="question and answers">


<div class="question js-question" data-questionid="73013700" data-position-on-page="0" data-score="0" id="question">
    <style>
    </style>
<div class="js-zone-container zone-container-main">
    <div id="dfp-tlb" class="everyonelovesstackoverflow everyoneloves__top-leaderboard everyoneloves__leaderboard"></div>
    <div class="js-report-ad-button-container " style="width: 728px"></div>
</div>

    <div class="post-layout">
        <div class="votecell post-layout--left">
            <div class="js-voting-container d-flex jc-center fd-column ai-stretch gs4 fc-black-200" data-post-id="73013700">
        <button class="js-vote-up-btn flex--item s-btn s-btn__unset c-pointer " data-controller="s-tooltip" data-s-tooltip-placement="right" aria-pressed="false" aria-label="Up vote" data-selected-classes="fc-theme-primary" data-unselected-classes="" aria-describedby="--stacks-s-tooltip-00mqn14f">
            <svg aria-hidden="true" class="svg-icon iconArrowUpLg" width="36" height="36" viewBox="0 0 36 36"><path d="M2 25h32L18 9 2 25Z"></path></svg>
        </button><div id="--stacks-s-tooltip-00mqn14f" class="s-popover s-popover__tooltip pe-none" aria-hidden="true" role="tooltip">This question shows research effort; it is useful and clear<div class="s-popover--arrow"></div></div>
        <div class="js-vote-count flex--item d-flex fd-column ai-center fc-black-500 fs-title" itemprop="upvoteCount" data-value="0">
            0
        </div>
        <button class="js-vote-down-btn flex--item s-btn s-btn__unset c-pointer " data-controller="s-tooltip" data-s-tooltip-placement="right" aria-pressed="false" aria-label="Down vote" data-selected-classes="fc-theme-primary" data-unselected-classes="" aria-describedby="--stacks-s-tooltip-4x71z9fr">
            <svg aria-hidden="true" class="svg-icon iconArrowDownLg" width="36" height="36" viewBox="0 0 36 36"><path d="M2 11h32L18 27 2 11Z"></path></svg>
        </button><div id="--stacks-s-tooltip-4x71z9fr" class="s-popover s-popover__tooltip pe-none" aria-hidden="true" role="tooltip">This question does not show any research effort; it is unclear or not useful<div class="s-popover--arrow"></div></div>

        <button class="js-bookmark-btn s-btn s-btn__unset c-pointer py4 js-gps-track" data-controller="s-tooltip" data-s-tooltip-placement="right" aria-pressed="false" aria-label="Bookmark" data-selected-classes="fc-yellow-600" data-gps-track="post.click({ item: 1, priv: 0, post_type: 1 })" aria-describedby="--stacks-s-tooltip-8gecz0wu">
            <svg aria-hidden="true" class="svg-icon iconBookmark" width="18" height="18" viewBox="0 0 18 18"><path d="M6 1a2 2 0 0 0-2 2v14l5-4 5 4V3a2 2 0 0 0-2-2H6Zm3.9 3.83h2.9l-2.35 1.7.9 2.77L9 7.59l-2.35 1.7.9-2.76-2.35-1.7h2.9L9 2.06l.9 2.77Z"></path></svg>
            <div class="js-bookmark-count mt4 d-none" data-value=""></div>
        </button><div id="--stacks-s-tooltip-8gecz0wu" class="s-popover s-popover__tooltip pe-none" aria-hidden="true" role="tooltip">Bookmark this question.<div class="s-popover--arrow"></div></div>



        <a class="js-post-issue flex--item s-btn s-btn__unset c-pointer py6 mx-auto" href="/posts/73013700/timeline" data-shortcut="T" data-ks-title="timeline" data-controller="s-tooltip" data-s-tooltip-placement="right" aria-label="Timeline" aria-describedby="--stacks-s-tooltip-93umax5d"><svg aria-hidden="true" class="mln2 mr0 svg-icon iconHistory" width="19" height="18" viewBox="0 0 19 18"><path d="M3 9a8 8 0 1 1 3.73 6.77L8.2 14.3A6 6 0 1 0 5 9l3.01-.01-4 4-4-4h3L3 9Zm7-4h1.01L11 9.36l3.22 2.1-.6.93L10 10V5Z"></path></svg></a><div id="--stacks-s-tooltip-93umax5d" class="s-popover s-popover__tooltip pe-none" aria-hidden="true" role="tooltip">Show activity on this post.<div class="s-popover--arrow"></div></div>

</div>

        </div>



<div class="postcell post-layout--right">

    <div class="s-prose js-post-body" itemprop="text">

<p>I'm working on a Django project. Right now (if you're the dev) you can make changes to the HTML pretty easily. i'm not having any issues with that, i just want to know how to get the server to reload when the HTML changes. here's the github.</p>
<p><a href="https://github.com/jeffcrockett86/django-unchained" rel="nofollow noreferrer">https://github.com/jeffcrockett86/django-unchained</a></p>
    </div>

        <div class="mt24 mb12">
            <div class="post-taglist d-flex gs4 gsy fd-column">
                <div class="d-flex ps-relative fw-wrap">
                    <a href="/questions/tagged/python" class="post-tag" title="show questions tagged 'python'" rel="tag">python</a> <a href="/questions/tagged/django" class="post-tag" title="show questions tagged 'django'" rel="tag">django</a>
                </div>
            </div>
        </div>

    <div class="mb0 ">
        <div class="mt16 d-flex gs8 gsy fw-wrap jc-end ai-start pt4 mb16">
            <div class="flex--item mr16 fl1 w96">



<div class="js-post-menu pt2" data-post-id="73013700">
    <div class="d-flex gs8 s-anchors s-anchors__muted fw-wrap">

            <div class="flex--item">
                <a href="/q/73013700" rel="nofollow" itemprop="url" class="js-share-link js-gps-track" title="Short permalink to this question" data-gps-track="post.click({ item: 2, priv: 0, post_type: 1 })" data-controller="se-share-sheet s-popover" data-se-share-sheet-title="Share a link to this question" data-se-share-sheet-subtitle="" data-se-share-sheet-post-type="question" data-se-share-sheet-social="facebook twitter devto" data-se-share-sheet-location="1" data-se-share-sheet-license-url="https%3a%2f%2fcreativecommons.org%2flicenses%2fby-sa%2f4.0%2f" data-se-share-sheet-license-name="CC BY-SA 4.0" data-s-popover-placement="bottom-start" aria-controls="se-share-sheet-0" data-action=" s-popover#toggle se-share-sheet#preventNavigation s-popover:show->se-share-sheet#willShow s-popover:shown->se-share-sheet#didShow" aria-expanded="false">Share</a><div class="s-popover z-dropdown s-anchors s-anchors__default" style="width: unset; max-width: 28em;" id="se-share-sheet-0"><div class="s-popover--arrow"></div><div><label class="js-title fw-bold" for="share-sheet-input-se-share-sheet-0">Share a link to this question</label> <span class="js-subtitle"></span></div><div class="my8"><input type="text" id="share-sheet-input-se-share-sheet-0" class="js-input s-input wmn3 sm:wmn-initial" readonly=""></div><div class="d-flex jc-space-between ai-center mbn4"><button class="js-copy-link-btn s-btn s-btn__link js-gps-track" data-gps-track="">Copy link</button><a href="https://creativecommons.org/licenses/by-sa/4.0/" rel="license" class="js-license s-block-link w-auto" target="_blank" title="The current license for this post: CC BY-SA 4.0">CC BY-SA 4.0</a><div class="js-social-container d-none"></div></div></div>
            </div>



            <div class="flex--item">
                <button type="button" id="btnFollowPost-73013700" class="s-btn s-btn__link js-follow-post js-follow-question js-gps-track" data-gps-track="post.click({ item: 14, priv: 0, post_type: 1 })" data-controller="s-tooltip " data-s-tooltip-placement="bottom" data-s-popover-placement="bottom" aria-controls="" aria-describedby="--stacks-s-tooltip-phlnn3s7">
                    Follow
                </button><div id="--stacks-s-tooltip-phlnn3s7" class="s-popover s-popover__tooltip pe-none" aria-hidden="true" role="tooltip">Follow this question to receive notifications<div class="s-popover--arrow"></div></div>
            </div>






    </div>
    <div class="js-menu-popup-container"></div>
</div>
            </div>

            <div class="post-signature owner flex--item">
                <div class="user-info ">
    <div class="user-action-time">
        asked <span title="2022-07-17 16:53:28Z" class="relativetime">31 mins ago</span>
    </div>
    <div class="user-gravatar32">
        <a href="/users/8456701/jeff-crobotnik"><div class="gravatar-wrapper-32"><img src="https://www.gravatar.com/avatar/76343ce245d0ee70538e3ab4c94fc4c7?s=64&amp;d=identicon&amp;r=PG&amp;f=1" alt="user avatar" width="32" height="32" class="bar-sm"></div></a>
    </div>
    <div class="user-details" itemprop="author" itemscope="" itemtype="http://schema.org/Person">
        <a href="/users/8456701/jeff-crobotnik">Jeff Crobotnik</a><span class="d-none" itemprop="name">Jeff Crobotnik</span>
        <div class="-flair">
            <span class="reputation-score" title="reputation score " dir="ltr">1</span>
        </div>
    </div>
</div>

    <div class="js-new-contributor-indicator ps-relative">
        <div class="new-contributor-indicator fc-medium py6 px8 bbr-sm">
            <span class="js-new-contributor-label"><svg aria-hidden="true" class="svg-icon iconWave" width="18" height="18" viewBox="0 0 18 18"><path d="M10.7 17c-2.3 0-3.9-2.05-5.07-3.54l-.49-.6c-.67-.8-1.59-1.63-2.4-2.36A10.91 10.91 0 0 1 1.1 8.87a.79.79 0 0 1-.09-.56c.04-.19.14-.34.27-.4.14-.07.29-.1.45-.1.35 0 .67.18.87.34l3.5 2.75c.04.03.1.03.13 0a.09.09 0 0 0 .02-.13l-.02-.02c-.57-.8-3.42-4.77-3.71-5.15-.21-.27-.3-.58-.24-.84.05-.2.2-.37.4-.48.18-.09.35-.13.52-.13.44 0 .76.28.96.51l3.6 4.42c.04.04.07.06.14.02.05-.02.06-.07.03-.12L4.41 2.96a.94.94 0 0 1-.1-.73.92.92 0 0 1 .47-.57 1.06 1.06 0 0 1 1.4.39l3.8 6.14c.03.04.07.07.14.04.04-.03.06-.07.04-.13A153.8 153.8 0 0 0 8.1 2.54c-.31-.68-.2-1.14.36-1.42.52-.27 1.14-.07 1.47.48l3.69 8.3c.02.04.05.05.1.06a.1.1 0 0 0 .09-.07l.66-2.28c.1-.3.31-.56.62-.72.3-.15.65-.18.98-.1.7.2 1.09.87.89 1.52-.1.37-.46 1.73-.99 3.43l-.1.33c-.58 1.86-1.03 3.33-3.11 4.4-.7.35-1.38.53-2.05.53Z" fill="#FFC166"></path><path d="M14 .37a.5.5 0 0 0-.88.45l1.96 3.9a.5.5 0 0 0 .9-.45L14 .37Zm-1.17 2.17a.5.5 0 0 0-.91.42l.84 1.87a.5.5 0 1 0 .91-.41l-.84-1.88Zm-10.6 9.74a.5.5 0 0 1 .7-.02l1.7 1.6a.5.5 0 0 1-.7.72l-1.68-1.6a.5.5 0 0 1-.02-.7Zm-1.39.98a.5.5 0 1 0-.68.73l3.03 2.84a.5.5 0 0 0 .68-.73L.84 13.26Z" opacity=".4"></path></svg> New contributor</span>
        </div>
        <div class="js-new-contributor-popover s-popover fs-caption">
            <div class="s-popover--arrow s-popover--arrow__tc"></div>
            <a href="/users/8456701/jeff-crobotnik">Jeff Crobotnik</a> is a new contributor to this site. Take care in asking for clarification, commenting, and answering.
Check out our <a href="/conduct">Code of Conduct</a>.        </div>
    </div>

            </div>
        </div>
    </div>

</div>




            <span class="d-none" itemprop="commentCount"></span>
    <div class="post-layout--right js-post-comments-component">
        <div id="comments-73013700" class="comments js-comments-container bt bc-black-075 mt12  dno" data-post-id="73013700" data-min-length="15">
            <ul class="comments-list js-comments-list" data-remaining-comments-count="0" data-canpost="false" data-cansee="true" data-comments-unavailable="false" data-addlink-disabled="true">

            </ul>
	    </div>

        <div id="comments-link-73013700" data-rep="50" data-anon="true">
                    <a class="js-add-link comments-link disabled-link" title="Use comments to ask for more information or suggest improvements. Avoid answering questions in comments." href="#" role="button">Add a comment</a>
                <span class="js-link-separator dno">&nbsp;|&nbsp;</span>
            <a class="js-show-link comments-link dno" title="Expand to show all comments on this post" href="#" onclick="" role="button"></a>
        </div>
    </div>
    </div>

</div>


<div class="js-zone-container zone-container-responsive">
    <div id="dfp-isb" class="everyonelovesstackoverflow everyoneloves__inline-sidebar mx-auto"></div>
    <div class="js-report-ad-button-container mx-auto" style="width: 300px"></div>
</div>

                <div id="answers">
                    <a name="tab-top"></a>
                    <div id="answers-header">
                        <div class="answers-subheader d-flex ai-center mb8">
                            <div class="flex--item fl1">
                                <h2 class="mb0" data-answercount="1">
                                        1 Answer
                                    <span style="display:none;" itemprop="answerCount">1</span>
                                </h2>
                            </div>
                            <div class="flex--item">


<div class="d-flex g4 gsx ai-center sm:fd-column sm:ai-start">
    <div class="d-flex fd-column ai-end sm:ai-start">
        <label class="flex--item fs-caption" for="answer-sort-dropdown-select-menu">
            Sorted by:
        </label>
        <a class="js-sort-preference-change s-link flex--item fs-fine d-none" data-value="ScoreDesc" href="/questions/73013700/how-can-i-get-my-django-server-to-reload-when-i-change-the-html-in-dev-mode-with?answertab=scoredesc#tab-top">
            Reset to default
        </a>
    </div>
    <div class="flex--item s-select">
        <select id="answer-sort-dropdown-select-menu">
                    <option value="scoredesc" selected="selected">
                        Highest score (default)
                    </option>
                    <option value="trending">
                        Trending (recent votes count more)
                    </option>
                    <option value="modifieddesc">
                        Date modified (newest first)
                    </option>
                    <option value="createdasc">
                        Date created (oldest first)
                    </option>
        </select>
    </div>
</div>


                            </div>
                        </div>

                    </div>



<a name="73013747"></a>
<div id="answer-73013747" class="answer js-answer" data-answerid="73013747" data-parentid="73013700" data-score="0" data-position-on-page="1" data-highest-scored="1" data-question-has-accepted-highest-score="0" itemprop="acceptedAnswer" itemscope="" itemtype="https://schema.org/Answer">
    <div class="post-layout">
        <div class="votecell post-layout--left">
            <div class="js-voting-container d-flex jc-center fd-column ai-stretch gs4 fc-black-200" data-post-id="73013747">
        <button class="js-vote-up-btn flex--item s-btn s-btn__unset c-pointer " data-controller="s-tooltip" data-s-tooltip-placement="right" aria-pressed="false" aria-label="Up vote" data-selected-classes="fc-theme-primary" data-unselected-classes="" aria-describedby="--stacks-s-tooltip-1muumqcv">
            <svg aria-hidden="true" class="svg-icon iconArrowUpLg" width="36" height="36" viewBox="0 0 36 36"><path d="M2 25h32L18 9 2 25Z"></path></svg>
        </button><div id="--stacks-s-tooltip-1muumqcv" class="s-popover s-popover__tooltip pe-none" aria-hidden="true" role="tooltip">This answer is useful<div class="s-popover--arrow"></div></div>
        <div class="js-vote-count flex--item d-flex fd-column ai-center fc-black-500 fs-title" itemprop="upvoteCount" data-value="0">
            0
        </div>
        <button class="js-vote-down-btn flex--item s-btn s-btn__unset c-pointer " data-controller="s-tooltip" data-s-tooltip-placement="right" aria-pressed="false" aria-label="Down vote" data-selected-classes="fc-theme-primary" data-unselected-classes="" aria-describedby="--stacks-s-tooltip-edi77zpl">
            <svg aria-hidden="true" class="svg-icon iconArrowDownLg" width="36" height="36" viewBox="0 0 36 36"><path d="M2 11h32L18 27 2 11Z"></path></svg>
        </button><div id="--stacks-s-tooltip-edi77zpl" class="s-popover s-popover__tooltip pe-none" aria-hidden="true" role="tooltip">This answer is not useful<div class="s-popover--arrow"></div></div>


            <div class="js-accepted-answer-indicator flex--item fc-green-500 py6 mtn8 d-none" data-s-tooltip-placement="right" title="Loading when this answer was accepted…" tabindex="0" role="note" aria-label="Accepted">
                <div class="ta-center">
                    <svg aria-hidden="true" class="svg-icon iconCheckmarkLg" width="36" height="36" viewBox="0 0 36 36"><path d="m6 14 8 8L30 6v8L14 30l-8-8v-8Z"></path></svg>
                </div>
            </div>


        <a class="js-post-issue flex--item s-btn s-btn__unset c-pointer py6 mx-auto" href="/posts/73013747/timeline" data-shortcut="T" data-ks-title="timeline" data-controller="s-tooltip" data-s-tooltip-placement="right" aria-label="Timeline" aria-describedby="--stacks-s-tooltip-s4xejz11"><svg aria-hidden="true" class="mln2 mr0 svg-icon iconHistory" width="19" height="18" viewBox="0 0 19 18"><path d="M3 9a8 8 0 1 1 3.73 6.77L8.2 14.3A6 6 0 1 0 5 9l3.01-.01-4 4-4-4h3L3 9Zm7-4h1.01L11 9.36l3.22 2.1-.6.93L10 10V5Z"></path></svg></a><div id="--stacks-s-tooltip-s4xejz11" class="s-popover s-popover__tooltip pe-none" aria-hidden="true" role="tooltip">Show activity on this post.<div class="s-popover--arrow"></div></div>

</div>

        </div>



<div class="answercell post-layout--right">

    <div class="s-prose js-post-body" itemprop="text">
<p>You could have the client poll the server (eg. every 10 seconds). The server could then respond with a timestamp (e.g. unix millis). If the time is after the client was loaded (you could have the server put this in an <code>&lt;input type=hidden&gt;</code>, the client runs <code>window.location.reload();</code></p>
    </div>
    <div class="mt24">
        <div class="d-flex fw-wrap ai-start jc-end gs8 gsy">
            <time itemprop="dateCreated" datetime="2022-07-17T17:00:23"></time>
            <div class="flex--item mr16" style="flex: 1 1 100px;">



<div class="js-post-menu pt2" data-post-id="73013747">
    <div class="d-flex gs8 s-anchors s-anchors__muted fw-wrap">

            <div class="flex--item">
                <a href="/a/73013747" rel="nofollow" itemprop="url" class="js-share-link js-gps-track" title="Short permalink to this answer" data-gps-track="post.click({ item: 2, priv: 0, post_type: 2 })" data-controller="se-share-sheet s-popover" data-se-share-sheet-title="Share a link to this answer" data-se-share-sheet-subtitle="" data-se-share-sheet-post-type="answer" data-se-share-sheet-social="facebook twitter devto" data-se-share-sheet-location="2" data-se-share-sheet-license-url="https%3a%2f%2fcreativecommons.org%2flicenses%2fby-sa%2f4.0%2f" data-se-share-sheet-license-name="CC BY-SA 4.0" data-s-popover-placement="bottom-start" aria-controls="se-share-sheet-1" data-action=" s-popover#toggle se-share-sheet#preventNavigation s-popover:show->se-share-sheet#willShow s-popover:shown->se-share-sheet#didShow" aria-expanded="false">Share</a><div class="s-popover z-dropdown s-anchors s-anchors__default" style="width: unset; max-width: 28em;" id="se-share-sheet-1"><div class="s-popover--arrow"></div><div><label class="js-title fw-bold" for="share-sheet-input-se-share-sheet-1">Share a link to this answer</label> <span class="js-subtitle"></span></div><div class="my8"><input type="text" id="share-sheet-input-se-share-sheet-1" class="js-input s-input wmn3 sm:wmn-initial" readonly=""></div><div class="d-flex jc-space-between ai-center mbn4"><button class="js-copy-link-btn s-btn s-btn__link js-gps-track" data-gps-track="">Copy link</button><a href="https://creativecommons.org/licenses/by-sa/4.0/" rel="license" class="js-license s-block-link w-auto" target="_blank" title="The current license for this post: CC BY-SA 4.0">CC BY-SA 4.0</a><div class="js-social-container d-none"></div></div></div>
            </div>



            <div class="flex--item">
                <button type="button" id="btnFollowPost-73013747" class="s-btn s-btn__link js-follow-post js-follow-answer js-gps-track" data-gps-track="post.click({ item: 14, priv: 0, post_type: 2 })" data-controller="s-tooltip " data-s-tooltip-placement="bottom" data-s-popover-placement="bottom" aria-controls="" aria-describedby="--stacks-s-tooltip-2jhtvz9h">
                    Follow
                </button><div id="--stacks-s-tooltip-2jhtvz9h" class="s-popover s-popover__tooltip pe-none" aria-hidden="true" role="tooltip">Follow this answer to receive notifications<div class="s-popover--arrow"></div></div>
            </div>






    </div>
    <div class="js-menu-popup-container"></div>
</div>
            </div>


            <div class="post-signature flex--item fl0">
                <div class="user-info ">
    <div class="user-action-time">
        answered <span title="2022-07-17 17:00:23Z" class="relativetime">24 mins ago</span>
    </div>
    <div class="user-gravatar32">
        <a href="/users/18122498/jaffa"><div class="gravatar-wrapper-32"><img src="https://www.gravatar.com/avatar/af95943abd2d0c8a4c3508c9ae2ffa6c?s=64&amp;d=identicon&amp;r=PG" alt="user avatar" width="32" height="32" class="bar-sm"></div></a>
    </div>
    <div class="user-details" itemprop="author" itemscope="" itemtype="http://schema.org/Person">
        <a href="/users/18122498/jaffa">Jaffa</a><span class="d-none" itemprop="name">Jaffa</span>
        <div class="-flair">
            <span class="reputation-score" title="reputation score " dir="ltr">26</span><span title="4 bronze badges" aria-hidden="true"><span class="badge3"></span><span class="badgecount">4</span></span><span class="v-visible-sr">4 bronze badges</span>
        </div>
    </div>
</div>


            </div>
        </div>


    </div>

</div>




            <span class="d-none" itemprop="commentCount"></span>
    <div class="post-layout--right js-post-comments-component">
        <div id="comments-73013747" class="comments js-comments-container bt bc-black-075 mt12  dno" data-post-id="73013747" data-min-length="15">
            <ul class="comments-list js-comments-list" data-remaining-comments-count="0" data-canpost="false" data-cansee="true" data-comments-unavailable="false" data-addlink-disabled="true">

            </ul>
	    </div>

        <div id="comments-link-73013747" data-rep="50" data-anon="true">
                    <a class="js-add-link comments-link disabled-link" title="Use comments to ask for more information or suggest improvements. Avoid comments like “+1” or “thanks”." href="#" role="button">Add a comment</a>
                <span class="js-link-separator dno">&nbsp;|&nbsp;</span>
            <a class="js-show-link comments-link dno" title="Expand to show all comments on this post" href="#" onclick="" role="button"></a>
        </div>
    </div>
    </div>
</div>
<div class="js-zone-container zone-container-main">
    <div id="dfp-bmlb" class="everyonelovesstackoverflow everyoneloves__bot-mid-leaderboard everyoneloves__leaderboard"></div>
    <div class="js-report-ad-button-container " style="width: 728px"></div>
</div>

                        <a name="new-answer"></a>
                            <form id="post-form" action="/questions/73013700/answer/submit" method="post" class="js-add-answer-component post-form">
                                <input type="hidden" id="post-id" value="73013700">
                                <input type="hidden" id="qualityBanWarningShown" name="qualityBanWarningShown" value="false">
                                <input type="hidden" name="referrer" value="">
                                <h2 class="space">
                                    Your Answer
                                </h2>


    <script>
        StackExchange.ifUsing("editor", function () {
            StackExchange.using("externalEditor", function () {
                StackExchange.using("snippets", function () {
                    StackExchange.snippets.init();
                });
            });
        }, "code-snippets");
    </script>


<script>
    StackExchange.ready(function() {
        var channelOptions = {
            tags: "".split(" "),
            id: "1"
        };
        initTagRenderer("".split(" "), "".split(" "), channelOptions);

        StackExchange.using("externalEditor", function() {
            // Have to fire editor after snippets, if snippets enabled
            if (StackExchange.settings.snippets.snippetsEnabled) {
                StackExchange.using("snippets", function() {
                    createEditor();
                });
            }
            else {
                createEditor();
            }
        });

        function createEditor() {
            StackExchange.prepareEditor({
                useStacksEditor: false,
                heartbeatType: 'answer',
                autoActivateHeartbeat: false,
                convertImagesToLinks: true,
                noModals: true,
                showLowRepImageUploadWarning: true,
                reputationToPostImages: 10,
                bindNavPrevention: true,
                postfix: "",
                imageUploader: {
                    brandingHtml: "Powered by \u003ca href=\"https://imgur.com/\"\u003e\u003csvg class=\"svg-icon\" width=\"50\" height=\"18\" viewBox=\"0 0 50 18\" fill=\"none\" xmlns=\"http://www.w3.org/2000/svg\"\u003e\u003ctitle\u003eImgur Logo\u003c/title\u003e\u003cpath d=\"M46.1709 9.17788C46.1709 8.26454 46.2665 7.94324 47.1084 7.58816C47.4091 7.46349 47.7169 7.36433 48.0099 7.26993C48.9099 6.97997 49.672 6.73443 49.672 5.93063C49.672 5.22043 48.9832 4.61182 48.1414 4.61182C47.4335 4.61182 46.7256 4.91628 46.0943 5.50789C45.7307 4.9328 45.2525 4.66231 44.6595 4.66231C43.6264 4.66231 43.1481 5.28821 43.1481 6.59048V11.9512C43.1481 13.2535 43.6264 13.8962 44.6595 13.8962C45.6924 13.8962 46.1709 13.2535 46.1709 11.9512V9.17788Z\"/\u003e\u003cpath d=\"M32.492 10.1419C32.492 12.6954 34.1182 14.0484 37.0451 14.0484C39.9723 14.0484 41.5985 12.6954 41.5985 10.1419V6.59049C41.5985 5.28821 41.1394 4.66232 40.1061 4.66232C39.0732 4.66232 38.5948 5.28821 38.5948 6.59049V9.60062C38.5948 10.8521 38.2696 11.5455 37.0451 11.5455C35.8209 11.5455 35.4954 10.8521 35.4954 9.60062V6.59049C35.4954 5.28821 35.0173 4.66232 34.0034 4.66232C32.9703 4.66232 32.492 5.28821 32.492 6.59049V10.1419Z\" /\u003e\u003cpath fill-rule=\"evenodd\" clip-rule=\"evenodd\" d=\"M25.6622 17.6335C27.8049 17.6335 29.3739 16.9402 30.2537 15.6379C30.8468 14.7755 30.9615 13.5579 30.9615 11.9512V6.59049C30.9615 5.28821 30.4833 4.66231 29.4502 4.66231C28.9913 4.66231 28.4555 4.94978 28.1109 5.50789C27.499 4.86533 26.7335 4.56087 25.7005 4.56087C23.1369 4.56087 21.0134 6.57349 21.0134 9.27932C21.0134 11.9852 23.003 13.913 25.3754 13.913C26.5612 13.913 27.4607 13.4902 28.1109 12.6616C28.1109 12.7229 28.1161 12.7799 28.121 12.8346C28.1256 12.8854 28.1301 12.9342 28.1301 12.983C28.1301 14.4373 27.2502 15.2321 25.777 15.2321C24.8349 15.2321 24.1352 14.9821 23.5661 14.7787C23.176 14.6393 22.8472 14.5218 22.5437 14.5218C21.7977 14.5218 21.2429 15.0123 21.2429 15.6887C21.2429 16.7375 22.9072 17.6335 25.6622 17.6335ZM24.1317 9.27932C24.1317 7.94324 24.9928 7.09766 26.1024 7.09766C27.2119 7.09766 28.0918 7.94324 28.0918 9.27932C28.0918 10.6321 27.2311 11.5116 26.1024 11.5116C24.9737 11.5116 24.1317 10.6491 24.1317 9.27932Z\"/\u003e\u003cpath d=\"M16.8045 11.9512C16.8045 13.2535 17.2637 13.8962 18.2965 13.8962C19.3298 13.8962 19.8079 13.2535 19.8079 11.9512V8.12928C19.8079 5.82936 18.4879 4.62866 16.4027 4.62866C15.1594 4.62866 14.279 4.98375 13.3609 5.88013C12.653 5.05154 11.6581 4.62866 10.3573 4.62866C9.34336 4.62866 8.57809 4.89931 7.9466 5.5079C7.58314 4.9328 7.10506 4.66232 6.51203 4.66232C5.47873 4.66232 5.00066 5.28821 5.00066 6.59049V11.9512C5.00066 13.2535 5.47873 13.8962 6.51203 13.8962C7.54479 13.8962 8.0232 13.2535 8.0232 11.9512V8.90741C8.0232 7.58817 8.44431 6.91179 9.53458 6.91179C10.5104 6.91179 10.893 7.58817 10.893 8.94108V11.9512C10.893 13.2535 11.3711 13.8962 12.4044 13.8962C13.4375 13.8962 13.9157 13.2535 13.9157 11.9512V8.90741C13.9157 7.58817 14.3365 6.91179 15.4269 6.91179C16.4027 6.91179 16.8045 7.58817 16.8045 8.94108V11.9512Z\"/\u003e\u003cpath d=\"M3.31675 6.59049C3.31675 5.28821 2.83866 4.66232 1.82471 4.66232C0.791758 4.66232 0.313354 5.28821 0.313354 6.59049V11.9512C0.313354 13.2535 0.791758 13.8962 1.82471 13.8962C2.85798 13.8962 3.31675 13.2535 3.31675 11.9512V6.59049Z\" /\u003e\u003cpath d=\"M1.87209 0.400291C0.843612 0.400291 0 1.1159 0 1.98861C0 2.87869 0.822846 3.57676 1.87209 3.57676C2.90056 3.57676 3.7234 2.87869 3.7234 1.98861C3.7234 1.1159 2.90056 0.400291 1.87209 0.400291Z\" fill=\"#1BB76E\"/\u003e\u003c/svg\u003e\u003c/a\u003e",
                    contentPolicyHtml: "User contributions licensed under \u003ca href=\"https://stackoverflow.com/help/licensing\"\u003ecc by-sa\u003c/a\u003e \u003ca href=\"https://stackoverflow.com/legal/content-policy\"\u003e(content policy)\u003c/a\u003e",
                    allowUrls: true
                },
                onDemand: true,
                discardSelector: ".discard-answer"
                ,immediatelyShowMarkdownHelp:true,enableTables:true,enableSnippets:true
            });
                    }
    });
</script>
<div id="post-editor" class="post-editor js-post-editor">


        <div class="ps-relative">
            <div class="wmd-container mb8">
                <div id="wmd-button-bar" class="wmd-button-bar btr-sm"><ul id="wmd-button-row" class="wmd-button-row"><li id="wmd-bold-button" class="wmd-button" style="left: 0px;"><span style="background-position: 0px -20px;"></span></li><li id="wmd-italic-button" class="wmd-button" style="left: 25px;"><span style="background-position: -20px -20px;"></span></li><li id="wmd-spacer1" class="wmd-spacer" style="left: 50px;"><span style="background-position: -40px -20px;"></span></li><li id="wmd-link-button" class="wmd-button" style="left: 75px;"><span style="background-position: -40px -20px;"></span></li><li id="wmd-quote-button" class="wmd-button" style="left: 100px;"><span style="background-position: -60px -20px;"></span></li><li id="wmd-code-button" class="wmd-button" style="left: 125px;"><span style="background-position: -80px -20px;"></span></li><li id="wmd-image-button" class="wmd-button" style="left: 150px;"><span style="background-position: -100px -20px;"></span></li><li id="wmd-spacer2" class="wmd-spacer" style="left: 175px;"><span style="background-position: -120px -20px;"></span></li><li id="wmd-olist-button" class="wmd-button" style="left: 200px;"><span style="background-position: -120px -20px;"></span></li><li id="wmd-ulist-button" class="wmd-button" style="left: 225px;"><span style="background-position: -140px -20px;"></span></li><li id="wmd-heading-button" class="wmd-button" style="left: 250px;"><span style="background-position: -160px -20px;"></span></li><li id="wmd-hr-button" class="wmd-button" style="left: 275px;"><span style="background-position: -180px -20px;"></span></li><li id="wmd-spacer3" class="wmd-spacer" style="left: 300px;"><span style="background-position: -200px -20px;"></span></li><li id="wmd-undo-button" class="wmd-button" style="left: 325px;"><span style="background-position: -200px -20px;"></span></li><li id="wmd-redo-button" class="wmd-button" style="left: 350px;"><span style="background-position: -220px -20px;"></span></li><li class="wmd-spacer wmd-spacer-max"></li></ul></div>
                    <div class="new-contributor-indicator fc-black py12 ta-center bl br bc-black-200">
                        <svg aria-hidden="true" class="svg-icon iconWave" width="18" height="18" viewBox="0 0 18 18"><path d="M10.7 17c-2.3 0-3.9-2.05-5.07-3.54l-.49-.6c-.67-.8-1.59-1.63-2.4-2.36A10.91 10.91 0 0 1 1.1 8.87a.79.79 0 0 1-.09-.56c.04-.19.14-.34.27-.4.14-.07.29-.1.45-.1.35 0 .67.18.87.34l3.5 2.75c.04.03.1.03.13 0a.09.09 0 0 0 .02-.13l-.02-.02c-.57-.8-3.42-4.77-3.71-5.15-.21-.27-.3-.58-.24-.84.05-.2.2-.37.4-.48.18-.09.35-.13.52-.13.44 0 .76.28.96.51l3.6 4.42c.04.04.07.06.14.02.05-.02.06-.07.03-.12L4.41 2.96a.94.94 0 0 1-.1-.73.92.92 0 0 1 .47-.57 1.06 1.06 0 0 1 1.4.39l3.8 6.14c.03.04.07.07.14.04.04-.03.06-.07.04-.13A153.8 153.8 0 0 0 8.1 2.54c-.31-.68-.2-1.14.36-1.42.52-.27 1.14-.07 1.47.48l3.69 8.3c.02.04.05.05.1.06a.1.1 0 0 0 .09-.07l.66-2.28c.1-.3.31-.56.62-.72.3-.15.65-.18.98-.1.7.2 1.09.87.89 1.52-.1.37-.46 1.73-.99 3.43l-.1.33c-.58 1.86-1.03 3.33-3.11 4.4-.7.35-1.38.53-2.05.53Z" fill="#FFC166"></path><path d="M14 .37a.5.5 0 0 0-.88.45l1.96 3.9a.5.5 0 0 0 .9-.45L14 .37Zm-1.17 2.17a.5.5 0 0 0-.91.42l.84 1.87a.5.5 0 1 0 .91-.41l-.84-1.88Zm-10.6 9.74a.5.5 0 0 1 .7-.02l1.7 1.6a.5.5 0 0 1-.7.72l-1.68-1.6a.5.5 0 0 1-.02-.7Zm-1.39.98a.5.5 0 1 0-.68.73l3.03 2.84a.5.5 0 0 0 .68-.73L.84 13.26Z" opacity=".4"></path></svg>
                        <a href="/users/8456701/jeff-crobotnik">Jeff Crobotnik</a> is a new contributor. Be nice, and check out our <a href="/conduct">Code of Conduct</a>.
                    </div>
                <div class="js-stacks-validation">
                    <div class="ps-relative">
                        <textarea id="wmd-input" name="post-text" class="wmd-input s-input bar0 js-post-body-field" data-post-type-id="2" cols="92" rows="15" tabindex="101" data-min-length=""></textarea>
                    </div>
                    <div class="s-input-message mt4 d-none js-stacks-validation-message"></div>
                </div>
            </div>
        </div>

    <aside class="d-flex ai-start jc-space-between js-answer-help s-notice s-notice__warning pb0 pr4 pt4 mb8 d-none" role="status" aria-hidden="true">
    <div class="flex--item pt8">
        <p>Thanks for contributing an answer to Stack Overflow!</p><ul><li>Please be sure to <em>answer the question</em>. Provide details and share your research!</li></ul><p>But <em>avoid</em> …</p><ul><li>Asking for help, clarification, or responding to other answers.</li><li>Making statements based on opinion; back them up with references or personal experience.</li></ul><p>To learn more, see our <a href="/help/how-to-answer">tips on writing great answers</a>.</p>
    </div>
    <button class="flex--item js-answer-help-close-btn s-btn s-btn__muted fc-dark">
        <svg aria-hidden="true" class="svg-icon iconClear" width="18" height="18" viewBox="0 0 18 18"><path d="M15 4.41 13.59 3 9 7.59 4.41 3 3 4.41 7.59 9 3 13.59 4.41 15 9 10.41 13.59 15 15 13.59 10.41 9 15 4.41Z"></path></svg>
    </button>
</aside>



    <div>
        <div id="draft-saved" class="fc-success h24" style="display:none;">Draft saved</div>
        <div id="draft-discarded" class="fc-error h24" style="display:none;">Draft discarded</div>
    </div>


            <div id="wmd-preview" class="s-prose mb16 wmd-preview js-wmd-preview"></div>
            <div></div>

        <div class="edit-block">
            <input id="fkey" name="fkey" type="hidden" value="a1652ef8742c146baba5659e062cb0b54f183b9d298ed240b4cdb062a0535d03">
            <input id="author" name="author" type="text">
        </div>

</div>


                                <div class="ps-relative">
                                                <div class="form-item new-post-login p0 my16">
                <div class="d-flex gs16 md:fd-column new-login-form">
                    <div class="d-flex fd-column w50 md:w-auto gsy gs8 jc-space-between new-login-left">
                        <h3 class="flex--item fs-title">Sign up or <a id="login-link" href="/users/login?ssrc=question_page&amp;returnurl=https%3a%2f%2fstackoverflow.com%2fquestions%2f73013700%2fhow-can-i-get-my-django-server-to-reload-when-i-change-the-html-in-dev-mode-with%23new-answer">log in</a></h3>
                        <script>
                            StackExchange.ready(function () {
                                StackExchange.helpers.onClickDraftSave('#login-link');
                            });
                        </script>
                        <div class="flex--item s-btn s-btn__muted s-btn__outlined s-btn__icon google-login" data-ga="[&quot;sign up&quot;,&quot;Sign Up Started - Google&quot;,&quot;New Post&quot;,null,null]">
                            <svg aria-hidden="true" class="native svg-icon iconGoogle" width="18" height="18" viewBox="0 0 18 18"><path d="M16.51 8H8.98v3h4.3c-.18 1-.74 1.48-1.6 2.04v2.01h2.6a7.8 7.8 0 0 0 2.38-5.88c0-.57-.05-.66-.15-1.18Z" fill="#4285F4"></path><path d="M8.98 17c2.16 0 3.97-.72 5.3-1.94l-2.6-2a4.8 4.8 0 0 1-7.18-2.54H1.83v2.07A8 8 0 0 0 8.98 17Z" fill="#34A853"></path><path d="M4.5 10.52a4.8 4.8 0 0 1 0-3.04V5.41H1.83a8 8 0 0 0 0 7.18l2.67-2.07Z" fill="#FBBC05"></path><path d="M8.98 4.18c1.17 0 2.23.4 3.06 1.2l2.3-2.3A8 8 0 0 0 1.83 5.4L4.5 7.49a4.77 4.77 0 0 1 4.48-3.3Z" fill="#EA4335"></path></svg> Sign up using Google
                        </div>
                        <div class="flex--item s-btn s-btn__muted s-btn__icon facebook-login" data-ga="[&quot;sign up&quot;,&quot;Sign Up Started - Facebook&quot;,&quot;New Post&quot;,null,null]">
                            <svg aria-hidden="true" class="svg-icon iconFacebook" width="18" height="18" viewBox="0 0 18 18"><path d="M3 1a2 2 0 0 0-2 2v12c0 1.1.9 2 2 2h12a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2H3Zm6.55 16v-6.2H7.46V8.4h2.09V6.61c0-2.07 1.26-3.2 3.1-3.2.88 0 1.64.07 1.87.1v2.16h-1.29c-1 0-1.19.48-1.19 1.18V8.4h2.39l-.31 2.42h-2.08V17h-2.5Z" fill="#4167B2"></path></svg> Sign up using Facebook
                        </div>
                        <div class="flex--item s-btn s-btn__muted s-btn__outlined s-btn__icon stackexchange-login" data-ga="[&quot;sign up&quot;,&quot;Sign Up Navigation&quot;,&quot;New Post&quot;,null,null]">
                            <svg aria-hidden="true" class="native svg-icon iconLogoGlyphXSm" width="18" height="18" viewBox="0 0 18 18"><path d="M14 16v-5h2v7H2v-7h2v5h10Z" fill="#BCBBBB"></path><path d="m12.09.72-1.21.9 4.5 6.07 1.22-.9L12.09.71ZM5 15h8v-2H5v2Zm9.15-5.87L8.35 4.3l.96-1.16 5.8 4.83-.96 1.16Zm-7.7-1.47 6.85 3.19.63-1.37-6.85-3.2-.63 1.38Zm6.53 5L5.4 11.39l.38-1.67 7.42 1.48-.22 1.46Z" fill="#F48024"></path></svg> Sign up using Email and Password
                        </div>
                    </div>
                    <input type="hidden" name="use-facebook" class="use-facebook" value="false">
                    <input type="hidden" name="use-google" class="use-google" value="false">
                    <button type="button" class="d-none js-submit-openid">Submit</button>
                    <div class="d-flex gsy gs8 fd-column w50 md:w-auto new-login-right form-item p0">
                                <h3 class="flex--item fs-title">Post as a guest</h3>
            <div class="flex--item">
                <div class="d-flex gs4 gsy fd-column">
                    <label class="s-label" for="display-name">Name</label>
                    <div class="d-flex ps-relative">
                        <input class="s-input" id="display-name" name="display-name" maxlength="30" type="text" value="" tabindex="105" placeholder="">
                    </div>
                </div>
            </div>
            <div class="flex--item">
                <div class="d-flex gs4 gsy fd-column">
                    <div class="flex--item">
                        <div class="d-flex gs2 gsy fd-column">
                            <label class="flex--item s-label" for="m-address">Email</label>
                            <p class="flex--item s-description">Required, but never shown</p>
                        </div>
                    </div>
                    <div class="d-flex ps-relative">
                        <input class="s-input js-post-email-field" id="m-address" name="m-address" type="text" value="" size="40" tabindex="106" placeholder="">
                    </div>
                </div>
            </div>

                    </div>
                </div>
            </div>
            <script>
                StackExchange.ready(
                    function () {
                        StackExchange.openid.initPostLogin('.new-post-login', 'https%3a%2f%2fstackoverflow.com%2fquestions%2f73013700%2fhow-can-i-get-my-django-server-to-reload-when-i-change-the-html-in-dev-mode-with%23new-answer', 'question_page');
                    }
                );
            </script>
            <noscript>
                        <h3 class="flex--item fs-title">Post as a guest</h3>
            <div class="flex--item">
                <div class="d-flex gs4 gsy fd-column">
                    <label class="s-label" for="display-name">Name</label>
                    <div class="d-flex ps-relative">
                        <input class="s-input" id="display-name" name="display-name" maxlength="30" type="text" value="" tabindex="105" placeholder="" />
                    </div>
                </div>
            </div>
            <div class="flex--item">
                <div class="d-flex gs4 gsy fd-column">
                    <div class="flex--item">
                        <div class="d-flex gs2 gsy fd-column">
                            <label class="flex--item s-label" for="m-address">Email</label>
                            <p class="flex--item s-description">Required, but never shown</p>
                        </div>
                    </div>
                    <div class="d-flex ps-relative">
                        <input class="s-input js-post-email-field" id="m-address" name="m-address" type="text" value="" size="40" tabindex="106" placeholder="" />
                    </div>
                </div>
            </div>

            </noscript>

                                </div>

                                    <div class="form-submit cbt d-flex gsx gs4">
                                        <button id="submit-button" class="flex--item s-btn s-btn__primary s-btn__icon" type="submit" tabindex="120" autocomplete="off">
Post Your Answer                                        </button>
                                        <button class="flex--item s-btn s-btn__danger discard-answer dno">
                                            Discard
                                        </button>
                                            <p class="privacy-policy-agreement">
                                                By clicking “Post Your Answer”, you agree to our <a href="https://stackoverflow.com/legal/terms-of-service/public" name="tos" target="_blank" class="-link">terms of service</a>, <a href="https://stackoverflow.com/legal/privacy-policy" name="privacy" target="_blank" class="-link">privacy policy</a> and <a href="https://stackoverflow.com/legal/cookie-policy" name="cookie" target="_blank" class="-link">cookie policy</a><input type="hidden" name="legalLinksShown" value="1">
                                            </p>
                                    </div>
                                    <div class="js-general-error general-error cbt d-none"></div>
                            </form>


                            <h2 class="bottom-notice" data-loc="1">
Not the answer you're looking for? Browse other questions tagged <a href="/questions/tagged/python" class="post-tag" title="show questions tagged 'python'" rel="tag">python</a> <a href="/questions/tagged/django" class="post-tag" title="show questions tagged 'django'" rel="tag">django</a>  or <a href="/questions/ask">ask your own question</a>.                            </h2>
                </div>
            </div>
            <div id="sidebar" class="show-votes" role="complementary" aria-label="sidebar">



<div class="s-sidebarwidget s-sidebarwidget__yellow s-anchors s-anchors__grayscale mb16" data-tracker="cb=1">
    <ul class="d-block p0 m0">
                    <div class="s-sidebarwidget--header s-sidebarwidget__small-bold-text fc-light d:fc-black-900 bb bbw1">
                        The Overflow Blog
                    </div>
        <li class="s-sidebarwidget--item d-flex px16">
            <div class="flex--item1 fl-shrink0">
<svg aria-hidden="true" class="va-text-top svg-icon iconPencilSm" width="14" height="14" viewBox="0 0 14 14"><path d="m11.1 1.71 1.13 1.12c.2.2.2.51 0 .71L11.1 4.7 9.21 2.86l1.17-1.15c.2-.2.51-.2.71 0ZM2 10.12l6.37-6.43 1.88 1.88L3.88 12H2v-1.88Z"></path></svg>            </div>
            <div class="flex--item wmn0 ow-break-word">
                <a href="https://stackoverflow.blog/2022/07/14/how-rust-manages-memory-using-ownership-and-borrowing/?cb=1" class="js-gps-track" data-ga="[&quot;community bulletin board&quot;,&quot;The Overflow Blog&quot;,&quot;https://stackoverflow.blog/2022/07/14/how-rust-manages-memory-using-ownership-and-borrowing/&quot;,null,null]" data-gps-track="communitybulletin.click({ priority: 1, position: 0 })">How Rust manages memory using ownership and borrowing</a>
            </div>
        </li>
        <li class="s-sidebarwidget--item d-flex px16">
            <div class="flex--item1 fl-shrink0">
<svg aria-hidden="true" class="va-text-top svg-icon iconPencilSm" width="14" height="14" viewBox="0 0 14 14"><path d="m11.1 1.71 1.13 1.12c.2.2.2.51 0 .71L11.1 4.7 9.21 2.86l1.17-1.15c.2-.2.51-.2.71 0ZM2 10.12l6.37-6.43 1.88 1.88L3.88 12H2v-1.88Z"></path></svg>            </div>
            <div class="flex--item wmn0 ow-break-word">
                <a href="https://stackoverflow.blog/2022/07/15/at-your-next-job-interview-you-ask-the-questions-ep-463/?cb=1" class="js-gps-track" data-ga="[&quot;community bulletin board&quot;,&quot;The Overflow Blog&quot;,&quot;https://stackoverflow.blog/2022/07/15/at-your-next-job-interview-you-ask-the-questions-ep-463/&quot;,null,null]" data-gps-track="communitybulletin.click({ priority: 1, position: 1 })">At your next job interview, you ask the questions (Ep. 463)</a>
            </div>
        </li>
                    <div class="s-sidebarwidget--header s-sidebarwidget__small-bold-text fc-light d:fc-black-900 bb bbw1">
                        Featured on Meta
                    </div>
        <li class="s-sidebarwidget--item d-flex px16">
            <div class="flex--item1 fl-shrink0">
<div class="favicon favicon-stackexchangemeta" title="Meta Stack Exchange"></div>            </div>
            <div class="flex--item wmn0 ow-break-word">
                <a href="https://meta.stackexchange.com/questions/380295/announcing-the-stacks-editor-beta-release?cb=1" class="js-gps-track" data-ga="[&quot;community bulletin board&quot;,&quot;Featured on Meta&quot;,&quot;https://meta.stackexchange.com/questions/380295/announcing-the-stacks-editor-beta-release&quot;,null,null]" data-gps-track="communitybulletin.click({ priority: 3, position: 2 })">Announcing the Stacks Editor Beta release!</a>
            </div>
        </li>
        <li class="s-sidebarwidget--item d-flex px16">
            <div class="flex--item1 fl-shrink0">
<div class="favicon favicon-stackoverflowmeta" title="Meta Stack Overflow"></div>            </div>
            <div class="flex--item wmn0 ow-break-word">
                <a href="https://meta.stackoverflow.com/questions/418767/trending-a-new-answer-sorting-option?cb=1" class="js-gps-track" data-ga="[&quot;community bulletin board&quot;,&quot;Featured on Meta&quot;,&quot;https://meta.stackoverflow.com/questions/418767/trending-a-new-answer-sorting-option&quot;,null,null]" data-gps-track="communitybulletin.click({ priority: 6, position: 3 })">Trending: A new answer sorting option</a>
            </div>
        </li>
        <li class="s-sidebarwidget--item d-flex px16">
            <div class="flex--item1 fl-shrink0">
<div class="favicon favicon-stackoverflowmeta" title="Meta Stack Overflow"></div>            </div>
            <div class="flex--item wmn0 ow-break-word">
                <a href="https://meta.stackoverflow.com/questions/417320/the-options-tag-is-being-burninated?cb=1" class="js-gps-track" data-ga="[&quot;community bulletin board&quot;,&quot;Featured on Meta&quot;,&quot;https://meta.stackoverflow.com/questions/417320/the-options-tag-is-being-burninated&quot;,null,null]" data-gps-track="communitybulletin.click({ priority: 6, position: 4 })">The [options] tag is being burninated</a>
            </div>
        </li>
    </ul>
</div>


<div class="js-zone-container zone-container-sidebar">
    <div id="dfp-tsb" class="everyonelovesstackoverflow everyoneloves__top-sidebar"></div>
    <div class="js-report-ad-button-container " style="width: 300px"></div>
</div>
<div class="js-zone-container zone-container-sidebar">
    <div id="dfp-msb" class="everyonelovesstackoverflow everyoneloves__mid-sidebar"></div>
    <div class="js-report-ad-button-container " style="width: 300px"></div>
</div>
<div id="hireme"></div>

                    <div class="module sidebar-related">
                        <h4 id="h-related">Related</h4>
                        <div class="related js-gps-related-questions" data-tracker="rq=1">
                                <div class="spacer">
                                    <a href="http://127.0.0.1:8000/q/573618?rq=1" title="Question score (upvotes - downvotes)">
                                        <div class="answer-votes answered-accepted large">568</div>
                                    </a>
                                    <a href="http://127.0.0.1:8000/questions/573618/set-up-a-scheduled-job?rq=1" class="question-hyperlink">Set up a scheduled job?</a>
                                </div>
                                <div class="spacer">
                                    <a href="http://127.0.0.1:8000/q/678236?rq=1" title="Question score (upvotes - downvotes)">
                                        <div class="answer-votes answered-accepted extra-large">1460</div>
                                    </a>
                                    <a href="http://127.0.0.1:8000/questions/678236/how-do-i-get-the-filename-without-the-extension-from-a-path-in-python?rq=1" class="question-hyperlink">How do I get the filename without the extension from a path in Python?</a>
                                </div>
                                <div class="spacer">
                                    <a href="http://127.0.0.1:8000/q/2345708?rq=1" title="Question score (upvotes - downvotes)">
                                        <div class="answer-votes answered-accepted large">468</div>
                                    </a>
                                    <a href="http://127.0.0.1:8000/questions/2345708/how-can-i-get-the-full-absolute-url-with-domain-in-django?rq=1" class="question-hyperlink">How can I get the full/absolute URL (with domain) in Django?</a>
                                </div>
                                <div class="spacer">
                                    <a href="http://127.0.0.1:8000/q/4271740?rq=1" title="Question score (upvotes - downvotes)">
                                        <div class="answer-votes answered-accepted large">844</div>
                                    </a>
                                    <a href="http://127.0.0.1:8000/questions/4271740/how-can-i-use-python-to-get-the-system-hostname?rq=1" class="question-hyperlink">How can I use Python to get the system hostname?</a>
                                </div>
                                <div class="spacer">
                                    <a href="http://127.0.0.1:8000/q/5364050?rq=1" title="Question score (upvotes - downvotes)">
                                        <div class="answer-votes answered-accepted large">480</div>
                                    </a>
                                    <a href="http://127.0.0.1:8000/questions/5364050/reloading-submodules-in-ipython?rq=1" class="question-hyperlink">Reloading submodules in IPython</a>
                                </div>
                                <div class="spacer">
                                    <a href="http://127.0.0.1:8000/q/6077675?rq=1" title="Question score (upvotes - downvotes)">
                                        <div class="answer-votes answered-accepted large">351</div>
                                    </a>
                                    <a href="http://127.0.0.1:8000/questions/6077675/why-am-i-seeing-typeerror-string-indices-must-be-integers?rq=1" class="question-hyperlink">Why am I seeing "TypeError: string indices must be integers"?</a>
                                </div>
                                <div class="spacer">
                                    <a href="http://127.0.0.1:8000/q/16344756?rq=1" title="Question score (upvotes - downvotes)">
                                        <div class="answer-votes answered-accepted large">332</div>
                                    </a>
                                    <a href="http://127.0.0.1:8000/questions/16344756/auto-reloading-python-flask-app-upon-code-changes?rq=1" class="question-hyperlink">Auto reloading python Flask app upon code changes</a>
                                </div>
                                <div class="spacer">
                                    <a href="http://127.0.0.1:8000/q/19743396?rq=1" title="Question score (upvotes - downvotes)">
                                        <div class="answer-votes answered-accepted large">428</div>
                                    </a>
                                    <a href="http://127.0.0.1:8000/questions/19743396/cors-cannot-use-wildcard-in-access-control-allow-origin-when-credentials-flag-i?rq=1" class="question-hyperlink">CORS: Cannot use wildcard in Access-Control-Allow-Origin when credentials flag is true</a>
                                </div>
                                <div class="spacer">
                                    <a href="http://127.0.0.1:8000/q/35158334?rq=1" title="Question score (upvotes - downvotes)">
                                        <div class="answer-votes default">4</div>
                                    </a>
                                    <a href="http://127.0.0.1:8000/questions/35158334/django-apply-changes-in-html-static-files-without-restarting-dev-server?rq=1" class="question-hyperlink">Django - Apply changes in HTML &amp; Static files without restarting dev server</a>
                                </div>
                                <div class="spacer">
                                    <a href="http://127.0.0.1:8000/q/72379283?rq=1" title="Question score (upvotes - downvotes)">
                                        <div class="answer-votes answered-accepted default">0</div>
                                    </a>
                                    <a href="http://127.0.0.1:8000/questions/72379283/django-dev-server-does-not-automatically-reload-after-saving-files?rq=1" class="question-hyperlink">Django dev server does not automatically reload after saving files</a>
                                </div>
                        </div>
                    </div>

                <div id="hot-network-questions" class="module tex2jax_ignore">
    <h4>
        <a href="https://stackexchange.com/questions?tab=hot" class="js-gps-track s-link s-link__inherit" data-gps-track="posts_hot_network.click({ item_type:1, location:11 })">
            Hot Network Questions
        </a>
    </h4>
    <ul>
            <li>
                <div class="favicon favicon-music" title="Music: Practice &amp; Theory Stack Exchange"></div><a href="https://music.stackexchange.com/questions/123868/why-do-musicians-play-too-loud-on-social-gatherings" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:240 }); posts_hot_network.click({ item_type:2, location:11 })">
                    Why do musicians play too loud on social gatherings?
                </a>

            </li>
            <li>
                <div class="favicon favicon-worldbuilding" title="Worldbuilding Stack Exchange"></div><a href="https://worldbuilding.stackexchange.com/questions/232836/how-quickly-can-a-disembodied-human-brain-space-travel-and-be-fine" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:579 }); posts_hot_network.click({ item_type:2, location:11 })">
                    How quickly can a disembodied human brain space travel and be fine?
                </a>

            </li>
            <li>
                <div class="favicon favicon-cooking" title="Seasoned Advice"></div><a href="https://cooking.stackexchange.com/questions/121069/why-does-my-curry-taste-flat" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:49 }); posts_hot_network.click({ item_type:2, location:11 })">
                    Why does my curry taste flat
                </a>

            </li>
            <li>
                <div class="favicon favicon-electronics" title="Electrical Engineering Stack Exchange"></div><a href="https://electronics.stackexchange.com/questions/627650/stm32-c-function-strstr-not-working" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:135 }); posts_hot_network.click({ item_type:2, location:11 })">
                    STM32 C function "strstr()" not working
                </a>

            </li>
            <li>
                <div class="favicon favicon-rpg" title="Role-playing Games Stack Exchange"></div><a href="https://rpg.stackexchange.com/questions/199974/does-any-source-published-prior-to-5th-edition-attest-that-strahd-von-zarovich-i" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:122 }); posts_hot_network.click({ item_type:2, location:11 })">
                    Does any source published prior to 5th Edition attest that Strahd von Zarovich is the first vampire ever?
                </a>

            </li>
            <li class="js-hidden dno" style="display: list-item;">
                <div class="favicon favicon-serverfault" title="Server Fault"></div><a href="https://serverfault.com/questions/1105694/how-to-restrict-passwordless-ssh" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:2 }); posts_hot_network.click({ item_type:2, location:11 })">
                    How to restrict passwordless SSH?
                </a>

            </li>
            <li class="js-hidden dno" style="display: list-item;">
                <div class="favicon favicon-math" title="Mathematics Stack Exchange"></div><a href="https://math.stackexchange.com/questions/4494439/find-the-number-of-permutations-of-the-word-aurobind-in-which-vowels-appear-in" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:69 }); posts_hot_network.click({ item_type:2, location:11 })">
                    Find the number of permutations of the word "AUROBIND" in which vowels appear in alphabetical order?
                </a>

            </li>
            <li class="js-hidden dno" style="display: list-item;">
                <div class="favicon favicon-scifi" title="Science Fiction &amp; Fantasy Stack Exchange"></div><a href="https://scifi.stackexchange.com/questions/265616/did-the-wild-men-actually-help-in-the-great-battle-in-the-return-of-the-king" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:186 }); posts_hot_network.click({ item_type:2, location:11 })">
                    Did the "Wild Men" actually help in the great battle in The Return of the King?
                </a>

            </li>
            <li class="js-hidden dno" style="">
                <div class="favicon favicon-law" title="Law Stack Exchange"></div><a href="https://law.stackexchange.com/questions/82222/could-we-understand-that-someone-who-is-still-innocent-until-proven-otherwise" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:617 }); posts_hot_network.click({ item_type:2, location:11 })">
                    Could we understand that someone who is still 'innocent until proven otherwise', be 'possibly' guilty?
                </a>

            </li>
            <li class="js-hidden dno" style="">
                <div class="favicon favicon-security" title="Information Security Stack Exchange"></div><a href="https://security.stackexchange.com/questions/263429/what-exactly-happens-when-i-validate-adigital-signature" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:162 }); posts_hot_network.click({ item_type:2, location:11 })">
                    What exactly happens when I "validate" adigital signature?
                </a>

            </li>
            <li class="js-hidden dno" style="">
                <div class="favicon favicon-mathematica" title="Mathematica Stack Exchange"></div><a href="https://mathematica.stackexchange.com/questions/270917/how-to-draw-a-pyramid-of-spheres-like-this" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:387 }); posts_hot_network.click({ item_type:2, location:11 })">
                    How to draw a pyramid of spheres like this?
                </a>

            </li>
            <li class="js-hidden dno" style="">
                <div class="favicon favicon-rpg" title="Role-playing Games Stack Exchange"></div><a href="https://rpg.stackexchange.com/questions/199982/if-a-guard-is-on-guard-should-the-active-perception-be-rolled-by-the-guard" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:122 }); posts_hot_network.click({ item_type:2, location:11 })">
                    If a guard is "on guard", should the "Active Perception" be rolled by the guard, instead of the "Passive Perception"?
                </a>

            </li>
            <li class="js-hidden dno" style="">
                <div class="favicon favicon-music" title="Music: Practice &amp; Theory Stack Exchange"></div><a href="https://music.stackexchange.com/questions/123852/solfege-why-dont-i-just-sing-the-numbers" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:240 }); posts_hot_network.click({ item_type:2, location:11 })">
                    Solfege - why don't I just sing the numbers?
                </a>

            </li>
            <li class="js-hidden dno" style="">
                <div class="favicon favicon-worldbuilding" title="Worldbuilding Stack Exchange"></div><a href="https://worldbuilding.stackexchange.com/questions/232809/how-to-set-up-exchange-rate-between-two-very-different-world" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:579 }); posts_hot_network.click({ item_type:2, location:11 })">
                    How to set up exchange rate between two very different world
                </a>

            </li>
            <li class="js-hidden dno" style="">
                <div class="favicon favicon-philosophy" title="Philosophy Stack Exchange"></div><a href="https://philosophy.stackexchange.com/questions/92255/is-there-a-name-for-this-type-of-fallacy" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:265 }); posts_hot_network.click({ item_type:2, location:11 })">
                    Is there a name for this type of fallacy?
                </a>

            </li>
            <li class="js-hidden dno" style="">
                <div class="favicon favicon-movies" title="Movies &amp; TV Stack Exchange"></div><a href="https://movies.stackexchange.com/questions/118077/what-is-the-significance-of-the-song-take-me-home-country-roads" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:367 }); posts_hot_network.click({ item_type:2, location:11 })">
                    What is the significance of the song "Take Me Home, Country Roads"?
                </a>

            </li>
            <li class="js-hidden dno" style="">
                <div class="favicon favicon-academia" title="Academia Stack Exchange"></div><a href="https://academia.stackexchange.com/questions/187049/how-can-i-find-a-mentor-not-a-supervisor" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:415 }); posts_hot_network.click({ item_type:2, location:11 })">
                    How can I find a mentor (not a supervisor)?
                </a>

            </li>
            <li class="js-hidden dno" style="">
                <div class="favicon favicon-blender" title="Blender Stack Exchange"></div><a href="https://blender.stackexchange.com/questions/269512/smooth-step-function-with-math-nodes" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:502 }); posts_hot_network.click({ item_type:2, location:11 })">
                    Smooth Step Function with Math Nodes
                </a>

            </li>
            <li class="js-hidden dno" style="">
                <div class="favicon favicon-stats" title="Cross Validated"></div><a href="https://stats.stackexchange.com/questions/582210/is-it-possible-that-x-and-y-are-uncorrelated-but-x-can-significantly-predict-y" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:65 }); posts_hot_network.click({ item_type:2, location:11 })">
                    Is it possible that X and Y are uncorrelated but X can significantly predict Y?
                </a>

            </li>
            <li class="js-hidden dno" style="">
                <div class="favicon favicon-blender" title="Blender Stack Exchange"></div><a href="https://blender.stackexchange.com/questions/269525/use-position-data-of-one-geometry-object-on-another" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:502 }); posts_hot_network.click({ item_type:2, location:11 })">
                    Use position data of one geometry object on another
                </a>

            </li>
            <li class="js-hidden dno" style="">
                <div class="favicon favicon-math" title="Mathematics Stack Exchange"></div><a href="https://math.stackexchange.com/questions/4494410/is-there-a-math-concept-or-terminology-for-complex-numbers-with-identical-imagin" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:69 }); posts_hot_network.click({ item_type:2, location:11 })">
                    Is there a math concept or terminology for complex numbers with identical imaginary part and opposite real part?
                </a>

            </li>
            <li class="js-hidden dno" style="">
                <div class="favicon favicon-english" title="English Language &amp; Usage Stack Exchange"></div><a href="https://english.stackexchange.com/questions/592017/when-do-we-need-to-use-to-here" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:97 }); posts_hot_network.click({ item_type:2, location:11 })">
                    When do we need to use "to" here?
                </a>

            </li>
            <li class="js-hidden dno" style="">
                <div class="favicon favicon-ell" title="English Language Learners Stack Exchange"></div><a href="https://ell.stackexchange.com/questions/318885/idiom-for-saying-something-doesnt-cost-a-lot-for-someone-rich" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:481 }); posts_hot_network.click({ item_type:2, location:11 })">
                    Idiom for saying something doesn't cost a lot for someone rich?
                </a>

            </li>
            <li class="js-hidden dno" style="">
                <div class="favicon favicon-bicycles" title="Bicycles Stack Exchange"></div><a href="https://bicycles.stackexchange.com/questions/84926/are-there-single-speed-electric-bikes-already" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:126 }); posts_hot_network.click({ item_type:2, location:11 })">
                    Are there single speed electric bikes already?
                </a>

            </li>
    </ul>

        <a href="#" class="show-more js-show-more js-gps-track" data-gps-track="posts_hot_network.click({ item_type:3, location:11 })">
            more hot questions
        </a>
</div>

                            <div id="feed-link" class="js-feed-link">
        <a href="/feeds/question/73013700" title="Feed of this question and its answers">
            <svg aria-hidden="true" class="fc-orange-400 svg-icon iconRss" width="18" height="18" viewBox="0 0 18 18"><path d="M3 1a2 2 0 0 0-2 2v12c0 1.1.9 2 2 2h12a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2H3Zm0 1.5c6.9 0 12.5 5.6 12.5 12.5H13C13 9.55 8.45 5 3 5V2.5Zm0 5c4.08 0 7.5 3.41 7.5 7.5H8c0-2.72-2.28-5-5-5V7.5Zm0 5c1.36 0 2.5 1.14 2.5 2.5H3v-2.5Z"></path></svg>
            Question feed
        </a>
    </div>
    <aside class="s-modal js-feed-link-modal" tabindex="-1" role="dialog" aria-labelledby="feed-modal-title" aria-describedby="feed-modal-description" aria-hidden="true">
        <div class="s-modal--dialog js-modal-dialog wmx4" role="document" data-controller="se-draggable">
            <h1 class="s-modal--header fw-bold js-first-tabbable c-move" id="feed-modal-title" data-se-draggable-target="handle" tabindex="0">
                Subscribe to RSS
            </h1>
            <div class="d-flex gs4 gsy fd-column">
                <div class="flex--item">
                    <label class="d-block s-label c-default" for="feed-url">
                        Question feed
                        <p class="s-description mt2" id="feed-modal-description">To subscribe to this RSS feed, copy and paste this URL into your RSS reader.</p>
                    </label>
                </div>
                <div class="d-flex ps-relative">
                    <input class="s-input" type="text" name="feed-url" id="feed-url" readonly="readonly" value="https://stackoverflow.com/feeds/question/73013700">
                    <svg aria-hidden="true" class="s-input-icon fc-orange-400 svg-icon iconRss" width="18" height="18" viewBox="0 0 18 18"><path d="M3 1a2 2 0 0 0-2 2v12c0 1.1.9 2 2 2h12a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2H3Zm0 1.5c6.9 0 12.5 5.6 12.5 12.5H13C13 9.55 8.45 5 3 5V2.5Zm0 5c4.08 0 7.5 3.41 7.5 7.5H8c0-2.72-2.28-5-5-5V7.5Zm0 5c1.36 0 2.5 1.14 2.5 2.5H3v-2.5Z"></path></svg>
                </div>
            </div>
            <a class="s-modal--close s-btn s-btn__muted js-modal-close js-last-tabbable" href="#" aria-label="Close">
                <svg aria-hidden="true" class="svg-icon iconClearSm" width="14" height="14" viewBox="0 0 14 14"><path d="M12 3.41 10.59 2 7 5.59 3.41 2 2 3.41 5.59 7 2 10.59 3.41 12 7 8.41 10.59 12 12 10.59 8.41 7 12 3.41Z"></path></svg>
            </a>
        </div>
    </aside>

            </div>
    </div>
<script>StackExchange.ready(function(){$.get('/posts/73013700/ivc/1b68');});</script>
<noscript><div><img src="/posts/73013700/ivc/1b68" class="dno" alt="" width="0" height="0"></div></noscript><div style="display:none" id="js-codeblock-lang">lang-py</div></div>


        </div>
    </div>



<script>;(()=>{function k(t){var a=e[t];if(void 0!==a)return a.exports;var s=e[t]={exports:{}};return n[t].call(s.exports,s,s.exports,k),s.exports}var n={291:function(Kt,e){var t;!function(e,t){"use strict";"object"==typeof Kt.exports?Kt.exports=e.document?t(e,!0):function(n){if(!n.document)throw new Error("jQuery requires a window with a document");return t(n)}:t(e)}("undefined"==typeof window?this:window,function(Zt,n){"use strict";function i(a,e,t){var n,s,i=(t=t||y).createElement("script");if(i.text=a,e)for(n in h)(s=e[n]||e.getAttribute&&e.getAttribute(n))&&i.setAttribute(n,s);t.head.appendChild(i).parentNode.removeChild(i)}function w(t){return null==t?t+"":"object"==typeof t||"function"==typeof t?c[u.call(t)]||"object":typeof t}function T(a){var o=!!a&&"length"in a&&a.length,s=w(a);return!dn(a)&&!v(a)&&("array"===s||0===o||"number"==typeof o&&0<o&&o-1 in a)}function S(n,e){return n.nodeName&&n.nodeName.toLowerCase()===e.toLowerCase()}function r(o,s,i){return dn(s)?ln.grep(o,function(t,e){return!!s.call(t,e,t)!==i}):s.nodeType?ln.grep(o,function(t){return t===s!==i}):"string"==typeof s?ln.filter(s,o,i):ln.grep(o,function(t){return-1<a.call(s,t)!==i})}function D(n,e){for(;(n=n[e])&&1!==n.nodeType;);return n}function q(t){return t}function I(t){throw t}function _(a,e,t,n){var o;try{a&&dn(o=a.promise)?o.call(a).done(e).fail(t):a&&dn(o=a.then)?o.call(a,e,t):e.apply(void 0,[a].slice(n))}catch(n){t.apply(void 0,[n])}}function W(){y.removeEventListener("DOMContentLoaded",W),Zt.removeEventListener("load",W),ln.ready()}function F(n,e){return e.toUpperCase()}function z(t){return t.replace(R,"ms-").replace(X,F)}function Y(){this.expando=ln.expando+Y.uid++}function G(a,e,t){var n;if(void 0===t&&1===a.nodeType)if(n="data-"+e.replace(K,"-$&").toLowerCase(),"string"==typeof(t=a.getAttribute(n))){try{t=function(t){return"true"===t||"false"!==t&&("null"===t?null:t===+t+""?+t:Q.test(t)?JSON.parse(t):t)}(t)}catch(t){}V.set(a,e,t)}else t=void 0;return t}function J(d,e,t,n){var r,i,o=20,a=n?function(){return n.cur()}:function(){return ln.css(d,e,"")},s=a(),p=t&&t[3]||(ln.cssNumber[e]?"":"px"),l=d.nodeType&&(ln.cssNumber[e]||"px"!==p&&+s)&&ee.exec(ln.css(d,e));if(l&&l[3]!==p){for(s/=2,p=p||l[3],l=+s||1;o--;)ln.style(d,e,l+p),0>=(1-i)*(1-(i=a()/s||.5))&&(o=0),l/=i;l*=2,ln.style(d,e,l+p),t=t||[]}return t&&(l=+l||+s||0,r=t[1]?l+(t[1]+1)*t[2]:+t[2],n&&(n.unit=p,n.start=l,n.end=r)),r}function ne(a){var e,t=a.ownerDocument,n=a.nodeName,o=re[n];return o||(e=t.body.appendChild(t.createElement(n)),o=ln.css(e,"display"),e.parentNode.removeChild(e),"none"===o&&(o="block"),re[n]=o,o)}function de(s,e){for(var t,n,r=[],i=0,o=s.length;i<o;i++)(n=s[i]).style&&(t=n.style.display,e?("none"===t&&(r[i]=U.get(n,"display")||null,r[i]||(n.style.display="")),""===n.style.display&&ie(n)&&(r[i]=ne(n))):"none"!==t&&(r[i]="none",U.set(n,"display",t)));for(i=0;i<o;i++)null!=r[i]&&(s[i].style.display=r[i]);return s}function pe(a,e){var t;return t=void 0===a.getElementsByTagName?void 0===a.querySelectorAll?[]:a.querySelectorAll(e||"*"):a.getElementsByTagName(e||"*"),void 0===e||e&&S(a,e)?ln.merge([a],t):t}function ce(a,e){for(var o=0,n=a.length;o<n;o++)U.set(a[o],"globalEval",!e||U.get(e[o],"globalEval"))}function xe(g,e,t,n,r){for(var i,o,a,s,u,l,c=e.createDocumentFragment(),f=[],d=0,p=g.length;d<p;d++)if((i=g[d])||0===i)if("object"===w(i))ln.merge(f,i.nodeType?[i]:i);else if(ye.test(i)){for(o=o||c.appendChild(e.createElement("div")),a=(ge.exec(i)||["",""])[1].toLowerCase(),s=me[a]||me._default,o.innerHTML=s[1]+ln.htmlPrefilter(i)+s[2],l=s[0];l--;)o=o.lastChild;ln.merge(f,o.childNodes),(o=c.firstChild).textContent=""}else f.push(e.createTextNode(i));for(c.textContent="",d=0;i=f[d++];)if(n&&-1<ln.inArray(i,n))r&&r.push(i);else if(u=ae(i),o=pe(c.appendChild(i),"script"),u&&ce(o),t)for(l=0;i=o[l++];)fe.test(i.type||"")&&t.push(i);return c}function Ce(){return!0}function we(){return!1}function Se(n,e){return n===function(){try{return y.activeElement}catch(t){}}()==("focus"===e)}function ke(d,e,l,p,r,c){var o,a;if("object"==typeof e){for(a in"string"!=typeof l&&(p=p||l,l=void 0),e)ke(d,a,l,p,e[a],c);return d}if(null==p&&null==r?(r=l,p=l=void 0):null==r&&("string"==typeof l?(r=p,p=void 0):(r=p,p=l,l=void 0)),!1===r)r=we;else if(!r)return d;return 1===c&&(o=r,r=function(t){return ln().off(t),o.apply(this,arguments)},r.guid=o.guid||(o.guid=ln.guid++)),d.each(function(){ln.event.add(this,e,r,p,l)})}function je(a,s,t){t?(U.set(a,s,!1),ln.event.add(a,s,{namespace:!1,handler:function(n){var e,a,i=U.get(this,s);if(!(1&n.isTrigger&&this[s]))i.length&&(U.set(this,s,{value:ln.event.trigger(ln.extend(i[0],ln.Event.prototype),i.slice(1),this)}),n.stopImmediatePropagation());else if(i.length)(ln.event.special[s]||{}).delegateType&&n.stopPropagation();else if(i=an.call(arguments),U.set(this,s,i),e=t(this,s),this[s](),i!==(a=U.get(this,s))||e?U.set(this,s,!1):a={},i!==a)return n.stopImmediatePropagation(),n.preventDefault(),a&&a.value}})):void 0===U.get(a,s)&&ln.event.add(a,s,Ce)}function Ne(n,e){return S(n,"table")&&S(11===e.nodeType?e.firstChild:e,"tr")&&ln(n).children("tbody")[0]||n}function He(t){return t.type=(null!==t.getAttribute("type"))+"/"+t.type,t}function Oe(t){return"true/"===(t.type||"").slice(0,5)?t.type=t.type.slice(5):t.removeAttribute("type"),t}function Pe(d,e){var t,n,r,i,o,a;if(1===e.nodeType){if(U.hasData(d)&&(a=U.get(d).events))for(r in U.remove(e,"handle events"),a)for(t=0,n=a[r].length;t<n;t++)ln.event.add(e,r,a[r][t]);V.hasData(d)&&(i=V.access(d),o=ln.extend({},i),V.set(e,o))}}function Re(a,e){var t=e.nodeName.toLowerCase();"input"===t&&he.test(a.type)?e.checked=a.checked:"input"!==t&&"textarea"!==t||(e.defaultValue=a.defaultValue)}function Ie(p,e,t,n){e=on(e);var r,u,o,a,s,l,c=0,f=p.length,d=e[0],m=dn(d);if(m||1<f&&"string"==typeof d&&!rn.checkClone&&Te.test(d))return p.each(function(a){var s=p.eq(a);m&&(e[0]=d.call(this,a,s.html())),Ie(s,e,t,n)});if(f&&(u=(r=xe(e,p[0].ownerDocument,!1,p,n)).firstChild,1===r.childNodes.length&&(r=u),u||n)){for(a=(o=ln.map(pe(r,"script"),He)).length;c<f;c++)s=r,c!=f-1&&(s=ln.clone(s,!0,!0),a&&ln.merge(o,pe(s,"script"))),t.call(p[c],s,c);if(a)for(l=o[o.length-1].ownerDocument,ln.map(o,Oe),c=0;c<a;c++)s=o[c],fe.test(s.type||"")&&!U.access(s,"globalEval")&&ln.contains(l,s)&&(s.src&&"module"!==(s.type||"").toLowerCase()?ln._evalUrl&&!s.noModule&&ln._evalUrl(s.src,{nonce:s.nonce||s.getAttribute("nonce")},l):i(s.textContent.replace(Ee,""),s,l))}return p}function Me(a,e,t){for(var n,s=e?ln.filter(e,a):a,i=0;null!=(n=s[i]);i++)t||1!==n.nodeType||ln.cleanData(pe(n)),n.parentNode&&(t&&ae(n)&&ce(pe(n,"script")),n.parentNode.removeChild(n));return a}function _e(d,e,t){var n,r,i,o,a=d.style;return(t=t||Le(d))&&(""!==(o=t.getPropertyValue(e)||t[e])||ae(d)||(o=ln.style(d,e)),!rn.pixelBoxStyles()&&De.test(o)&&Be.test(e)&&(n=a.width,r=a.minWidth,i=a.maxWidth,a.minWidth=a.maxWidth=a.width=o,o=t.width,a.width=n,a.minWidth=r,a.maxWidth=i)),void 0===o?o:o+""}function ze(n,e){return{get:function(){return n()?void delete this.get:(this.get=e).apply(this,arguments)}}}function Ue(t){return ln.cssProps[t]||Xe[t]||(t in Fe?t:Xe[t]=function(a){for(var e=a[0].toUpperCase()+a.slice(1),t=We.length;t--;)if((a=We[t]+e)in Fe)return a}(t)||t)}function Ye(a,e,t){var n=ee.exec(e);return n?tn(0,n[2]-(t||0))+(n[3]||"px"):e}function et(d,e,t,n,l,i){var o="width"===e?1:0,a=0,s=0;if(t===(n?"border":"content"))return 0;for(;4>o;o+=2)"margin"===t&&(s+=ln.css(d,t+te[o],!0,l)),n?("content"===t&&(s-=ln.css(d,"padding"+te[o],!0,l)),"margin"!==t&&(s-=ln.css(d,"border"+te[o]+"Width",!0,l))):(s+=ln.css(d,"padding"+te[o],!0,l),"padding"===t?a+=ln.css(d,"border"+te[o]+"Width",!0,l):s+=ln.css(d,"border"+te[o]+"Width",!0,l));return!n&&0<=i&&(s+=tn(0,$t(d["offset"+e[0].toUpperCase()+e.slice(1)]-i-s-a-.5))||0),s}function tt(d,e,t){var l=Le(d),r=(!rn.boxSizingReliable()||t)&&"border-box"===ln.css(d,"boxSizing",!1,l),i=r,o=_e(d,e,l),a="offset"+e[0].toUpperCase()+e.slice(1);if(De.test(o)){if(!t)return o;o="auto"}return(!rn.boxSizingReliable()&&r||!rn.reliableTrDimensions()&&S(d,"tr")||"auto"===o||!parseFloat(o)&&"inline"===ln.css(d,"display",!1,l))&&d.getClientRects().length&&(r="border-box"===ln.css(d,"boxSizing",!1,l),(i=a in d)&&(o=d[a])),(o=parseFloat(o)||0)+et(d,e,t||(r?"border":"content"),i,l,o)+"px"}function nt(a,e,t,n,o){return new nt.prototype.init(a,e,t,n,o)}function en(){Je&&(!1===y.hidden&&Zt.requestAnimationFrame?Zt.requestAnimationFrame(en):Zt.setTimeout(en,ln.fx.interval),ln.fx.tick())}function ut(){return Zt.setTimeout(function(){Ke=void 0}),Ke=Date.now()}function lt(a,o){var t,n=0,s={height:a};for(o=o?1:0;4>n;n+=2-o)s["margin"+(t=te[n])]=s["padding"+t]=a;return o&&(s.opacity=s.width=a),s}function ct(s,e,t){for(var n,r=(ft.tweeners[e]||[]).concat(ft.tweeners["*"]),i=0,o=r.length;i<o;i++)if(n=r[i].call(t,e,s))return n}function ft(d,p,h){var g,f,i=0,o=ft.prefilters.length,m=ln.Deferred().always(function(){delete a.elem}),a=function(){if(f)return!1;for(var e=Ke||ut(),t=tn(0,s.startTime+s.duration-e),n=1-(t/s.duration||0),i=0,o=s.tweens.length;i<o;i++)s.tweens[i].run(n);return m.notifyWith(d,[s,n,t]),1>n&&o?t:(o||m.notifyWith(d,[s,1,0]),m.resolveWith(d,[s]),!1)},s=m.promise({elem:d,props:ln.extend({},p),opts:ln.extend(!0,{specialEasing:{},easing:ln.easing._default},h),originalProperties:p,originalOptions:h,startTime:Ke||ut(),duration:h.duration,tweens:[],createTween:function(e,t){var n=ln.Tween(d,s.opts,e,t,s.opts.specialEasing[e]||s.opts.easing);return s.tweens.push(n),n},stop:function(e){var t=0,n=e?s.tweens.length:0;if(f)return this;for(f=!0;t<n;t++)s.tweens[t].run(1);return e?(m.notifyWith(d,[s,1,0]),m.resolveWith(d,[s,e])):m.rejectWith(d,[s,e]),this}}),r=s.props;for(function(s,e){var t,n,r,i,o;for(t in s)if(r=e[n=z(t)],i=s[t],Array.isArray(i)&&(r=i[1],i=s[t]=i[0]),t!==n&&(s[n]=i,delete s[t]),(o=ln.cssHooks[n])&&("expand"in o))for(t in i=o.expand(i),delete s[n],i)(t in s)||(s[t]=i[t],e[t]=r);else e[n]=r}(r,s.opts.specialEasing);i<o;i++)if(g=ft.prefilters[i].call(s,d,r,s.opts))return dn(g.stop)&&(ln._queueHooks(s.elem,s.opts.queue).stop=g.stop.bind(g)),g;return ln.map(r,ct,s),dn(s.opts.start)&&s.opts.start.call(d,s),s.progress(s.opts.progress).done(s.opts.done,s.opts.complete).fail(s.opts.fail).always(s.opts.always),ln.fx.timer(ln.extend(a,{elem:d,anim:s,queue:s.opts.queue})),s}function dt(t){return(t.match(P)||[]).join(" ")}function vt(t){return t.getAttribute&&t.getAttribute("class")||""}function yt(t){return Array.isArray(t)?t:"string"==typeof t&&t.match(P)||[]}function bt(a,e,o,n){if(Array.isArray(e))ln.each(e,function(e,t){o||wt.test(a)?n(a,t):bt(a+"["+("object"==typeof t&&null!=t?e:"")+"]",t,o,n)});else if(o||"object"!==w(e))n(a,e);else for(var t in e)bt(a+"["+t+"]",e[t],o,n)}function Dt(t){return function(e,a){"string"!=typeof e&&(a=e,e="*");var n,s=0,i=e.toLowerCase().match(P)||[];if(dn(a))for(;n=i[s++];)"+"===n[0]?(n=n.slice(1)||"*",(t[n]=t[n]||[]).unshift(a)):(t[n]=t[n]||[]).push(a)}}function Ft(d,p,t,n){function r(e){var o;return a[e]=!0,ln.each(d[e]||[],function(d,e){var s=e(p,t,n);return"string"!=typeof s||i||a[s]?i?!(o=s):void 0:(p.dataTypes.unshift(s),r(s),!1)}),o}var a={},i=d===Ot;return r(p.dataTypes[0])||!a["*"]&&r("*")}function Bt(a,e){var t,n,o=ln.ajaxSettings.flatOptions||{};for(t in e)void 0!==e[t]&&((o[t]?a:n||(n={}))[t]=e[t]);return n&&ln.extend(!0,a,n),a}var $t=Math.ceil,tn=Math.max,nn=[],o=Object.getPrototypeOf,an=nn.slice,on=nn.flat?function(t){return nn.flat.call(t)}:function(t){return nn.concat.apply([],t)},s=nn.push,a=nn.indexOf,c={},u=c.toString,sn=c.hasOwnProperty,d=sn.toString,p=d.call(Object),rn={},dn=function(t){return"function"==typeof t&&"number"!=typeof t.nodeType&&"function"!=typeof t.item},v=function(t){return null!=t&&t===t.window},y=Zt.document,h={type:!0,src:!0,nonce:!0,noModule:!0},g="3.6.0",ln=function(n,e){return new ln.fn.init(n,e)};ln.fn=ln.prototype={jquery:g,constructor:ln,length:0,toArray:function(){return an.call(this)},get:function(t){return null==t?an.call(this):0>t?this[t+this.length]:this[t]},pushStack:function(n){var e=ln.merge(this.constructor(),n);return e.prevObject=this,e},each:function(t){return ln.each(this,t)},map:function(a){return this.pushStack(ln.map(this,function(e,t){return a.call(e,t,e)}))},slice:function(){return this.pushStack(an.apply(this,arguments))},first:function(){return this.eq(0)},last:function(){return this.eq(-1)},even:function(){return this.pushStack(ln.grep(this,function(n,e){return(e+1)%2}))},odd:function(){return this.pushStack(ln.grep(this,function(n,e){return e%2}))},eq:function(a){var o=this.length,t=+a+(0>a?o:0);return this.pushStack(0<=t&&t<o?[this[t]]:[])},end:function(){return this.prevObject||this.constructor()},push:s,sort:nn.sort,splice:nn.splice},ln.extend=ln.fn.extend=function(){var d,e,t,n,r,i,o=arguments[0]||{},p=1,s=arguments.length,c=!1;for("boolean"==typeof o&&(c=o,o=arguments[p]||{},p++),"object"==typeof o||dn(o)||(o={}),p===s&&(o=this,p--);p<s;p++)if(null!=(d=arguments[p]))for(e in d)n=d[e],"__proto__"!==e&&o!==n&&(c&&n&&(ln.isPlainObject(n)||(r=Array.isArray(n)))?(t=o[e],i=r&&!Array.isArray(t)?[]:r||ln.isPlainObject(t)?t:{},r=!1,o[e]=ln.extend(c,i,n)):void 0!==n&&(o[e]=n));return o},ln.extend({expando:"jQuery"+(g+Math.random()).replace(/\D/g,""),isReady:!0,error:function(t){throw new Error(t)},noop:function(){},isPlainObject:function(a){var e,t;return a&&"[object Object]"===u.call(a)&&(!(e=o(a))||"function"==typeof(t=sn.call(e,"constructor")&&e.constructor)&&d.call(t)===p)},isEmptyObject:function(n){for(var e in n)return!1;return!0},globalEval:function(a,e,t){i(a,{nonce:e&&e.nonce},t)},each:function(a,e){var t,n=0;if(T(a))for(t=a.length;n<t&&!1!==e.call(a[n],n,a[n]);n++);else for(n in a)if(!1===e.call(a[n],n,a[n]))break;return a},makeArray:function(a,o){var t=o||[];return null!=a&&(T(Object(a))?ln.merge(t,"string"==typeof a?[a]:a):s.call(t,a)),t},inArray:function(o,e,t){return null==e?-1:a.call(e,o,t)},merge:function(a,e){for(var t=+e.length,n=0,o=a.length;n<t;n++)a[o++]=e[n];return a.length=o,a},grep:function(a,e,t){for(var s=[],r=0,i=a.length;r<i;r++)!e(a[r],r)!==!t&&s.push(a[r]);return s},map:function(s,e,t){var n,r,i=0,o=[];if(T(s))for(n=s.length;i<n;i++)null!=(r=e(s[i],i,t))&&o.push(r);else for(i in s)null!=(r=e(s[i],i,t))&&o.push(r);return on(o)},guid:1,support:rn}),"function"==typeof Symbol&&(ln.fn[Symbol.iterator]=nn[Symbol.iterator]),ln.each(["Boolean","Number","String","Function","Array","Date","RegExp","Object","Error","Symbol"],function(n,e){c["[object "+e+"]"]=e.toLowerCase()});var f=function(_){function W(n,a,t,u){var g,o,s,l,c,f,h,b=a&&a.ownerDocument,y=a?a.nodeType:9;if(t=t||[],"string"!=typeof n||!n||1!==y&&9!==y&&11!==y)return t;if(!u&&(De(a),a=a||d,Le)){if(11!==y&&(c=U.exec(n)))if(!(g=c[1])){if(c[2])return k.apply(t,a.getElementsByTagName(n)),t;if((g=c[3])&&Ee.getElementsByClassName&&a.getElementsByClassName)return k.apply(t,a.getElementsByClassName(g)),t}else if(9===y){if(!(s=a.getElementById(g)))return t;if(s.id===g)return t.push(s),t}else if(b&&(s=b.getElementById(g))&&qe(a,s)&&s.id===g)return t.push(s),t;if(Ee.qsa&&!T[n+" "]&&(!p||!p.test(n))&&(1!==y||"object"!==a.nodeName.toLowerCase())){if(h=n,b=a,1===y&&(I.test(n)||O.test(n))){for((b=V.test(n)&&me(a.parentNode)||a)===a&&Ee.scope||((l=a.getAttribute("id"))?l=l.replace(K,J):a.setAttribute("id",l=He)),o=(f=r(n)).length;o--;)f[o]=(l?"#"+l:":scope")+" "+ye(f[o]);h=f.join(",")}try{return k.apply(t,b.querySelectorAll(h)),t}catch(e){T(n,!0)}finally{l===He&&a.removeAttribute("id")}}}return Ae(n.replace(H,"$1"),a,t,u)}function e(){var a=[];return function e(t,n){return a.push(t+" ")>ke.cacheLength&&delete e[a.shift()],e[t+" "]=n}}function se(t){return t[He]=!0,t}function ue(n){var e=d.createElement("fieldset");try{return!!n(e)}catch(t){return!1}finally{e.parentNode&&e.parentNode.removeChild(e),e=null}}function ce(a,e){for(var t=a.split("|"),n=t.length;n--;)ke.attrHandle[t[n]]=e}function fe(a,e){var t=e&&a,n=t&&1===a.nodeType&&1===e.nodeType&&a.sourceIndex-e.sourceIndex;if(n)return n;if(t)for(;t=t.nextSibling;)if(t===e)return-1;return a?1:-1}function de(n){return function(e){return"input"===e.nodeName.toLowerCase()&&e.type===n}}function pe(a){return function(e){var t=e.nodeName.toLowerCase();return("input"===t||"button"===t)&&e.type===a}}function he(n){return function(a){return"form"in a?a.parentNode&&!1===a.disabled?"label"in a?"label"in a.parentNode?a.parentNode.disabled===n:a.disabled===n:a.isDisabled===n||a.isDisabled!==!n&&ee(a)===n:a.disabled===n:"label"in a&&a.disabled===n}}function ge(s){return se(function(e){return e=+e,se(function(t,n){for(var r,i=s([],t.length,e),o=i.length;o--;)t[r=i[o]]&&(t[r]=!(n[r]=t[r]))})})}function me(t){return t&&void 0!==t.getElementsByTagName&&t}function ve(){}function ye(a){for(var e=0,t=a.length,n="";e<t;e++)n+=a[e].value;return n}function be(p,e,t){var h=e.dir,r=e.next,i=r||h,o=t&&"parentNode"===i,a=y++;return e.first?function(e,t,n){for(;e=e[h];)if(1===e.nodeType||o)return p(e,t,n);return!1}:function(e,t,n){var s,l,c,u=[Pe,a];if(n){for(;e=e[h];)if((1===e.nodeType||o)&&p(e,t,n))return!0;}else for(;e=e[h];)if(1===e.nodeType||o)if(l=(c=e[He]||(e[He]={}))[e.uniqueID]||(c[e.uniqueID]={}),r&&r===e.nodeName.toLowerCase())e=e[h]||e;else{if((s=l[i])&&s[0]===Pe&&s[1]===a)return u[2]=s[2];if(l[i]=u,u[2]=p(e,t,n))return!0}return!1}}function xe(a){return 1<a.length?function(e,t,n){for(var o=a.length;o--;)if(!a[o](e,t,n))return!1;return!0}:a[0]}function we(d,e,t,n,r){for(var i,o=[],a=0,s=d.length;a<s;a++)(i=d[a])&&(t&&!t(i,n,r)||(o.push(i),null!=e&&e.push(a)));return o}function Te(y,e,b,n,r,a){return n&&!n[He]&&(n=Te(n)),r&&!r[He]&&(r=Te(r,a)),se(function(i,x,a,s){var u,l,c,f=[],d=[],p=x.length,h=i||function(a,e,t){for(var n=0,o=e.length;n<o;n++)W(a,e[n],t);return t}(e||"*",a.nodeType?[a]:a,[]),g=y&&(i||!e)?we(h,f,y,a,s):h,m=b?r||(i?y:p||n)?[]:x:g;if(b&&b(g,m,a,s),n)for(u=we(m,d),n(u,[],a,s),l=u.length;l--;)(c=u[l])&&(m[d[l]]=!(g[d[l]]=c));if(!i)m=we(m===x?m.splice(p,m.length):m),r?r(null,x,m,s):k.apply(x,m);else if(r||y){if(r){for(u=[],l=m.length;l--;)(c=m[l])&&u.push(g[l]=c);r(null,m=[],u,s)}for(l=m.length;l--;)(c=m[l])&&-1<(u=r?A(i,c):f[l])&&(i[u]=!(x[u]=c))}})}function Ce(r){for(var l,e,t,n=r.length,o=ke.relative[r[0].type],i=o||ke.relative[" "],s=o?1:0,p=be(function(t){return t===l},i,!0),c=be(function(t){return-1<A(l,t)},i,!0),u=[function(t,e,n){var s=!o&&(n||e!==je)||((l=e).nodeType?p(t,e,n):c(t,e,n));return l=null,s}];s<n;s++)if(e=ke.relative[r[s].type])u=[be(xe(u),e)];else{if((e=ke.filter[r[s].type].apply(null,r[s].matches))[He]){for(t=++s;t<n&&!ke.relative[r[t].type];t++);return Te(1<s&&xe(u),1<s&&ye(r.slice(0,s-1).concat({value:" "===r[s-2].type?"*":""})).replace(H,"$1"),e,s<t&&Ce(r.slice(s,t)),t<n&&Ce(r=r.slice(t)),t<n&&ye(r))}u.push(e)}return xe(u)}var Se,Ee,ke,Ne,n,r,a,Ae,je,l,c,De,d,o,Le,p,s,u,qe,He="sizzle"+1*new Date,h=_.document,Pe=0,y=0,i=e(),b=e(),x=e(),T=e(),C=function(n,e){return n===e&&(c=!0),0},w={}.hasOwnProperty,t=[],S=t.pop,E=t.push,k=t.push,N=t.slice,A=function(a,e){for(var t=0,n=a.length;t<n;t++)if(a[t]===e)return t;return-1},j="checked|selected|async|autofocus|autoplay|controls|defer|disabled|hidden|ismap|loop|multiple|open|readonly|required|scoped",D="[\\x20\\t\\r\\n\\f]",L="(?:\\\\[\\da-fA-F]{1,6}[\\x20\\t\\r\\n\\f]?|\\\\[^\\r\\n\\f]|[\\w-]|[^\0-\\x7f])+",q=/[\x20\t\r\n\f]+/g,H=/^[\x20\t\r\n\f]+|((?:^|[^\\])(?:\\.)*)[\x20\t\r\n\f]+$/g,P=/^[\x20\t\r\n\f]*,[\x20\t\r\n\f]*/,O=/^[\x20\t\r\n\f]*([>+~]|[\x20\t\r\n\f])[\x20\t\r\n\f]*/,I=/[\x20\t\r\n\f]|>/,M=/:((?:\\[\da-fA-F]{1,6}[\x20\t\r\n\f]?|\\[^\r\n\f]|[\w-]|[^\0-\x7f])+)(?:\((('((?:\\.|[^\\'])*)'|"((?:\\.|[^\\"])*)")|((?:\\.|[^\\()[\]]|\[[\x20\t\r\n\f]*((?:\\[\da-fA-F]{1,6}[\x20\t\r\n\f]?|\\[^\r\n\f]|[\w-]|[^\0-\x7f])+)(?:[\x20\t\r\n\f]*([*^$|!~]?=)[\x20\t\r\n\f]*(?:'((?:\\.|[^\\'])*)'|"((?:\\.|[^\\"])*)"|((?:\\[\da-fA-F]{1,6}[\x20\t\r\n\f]?|\\[^\r\n\f]|[\w-]|[^\0-\x7f])+))|)[\x20\t\r\n\f]*\])*)|.*)\)|)/,B=/^(?:\\[\da-fA-F]{1,6}[\x20\t\r\n\f]?|\\[^\r\n\f]|[\w-]|[^\0-\x7f])+$/,R={ID:/^#((?:\\[\da-fA-F]{1,6}[\x20\t\r\n\f]?|\\[^\r\n\f]|[\w-]|[^\0-\x7f])+)/,CLASS:/^\.((?:\\[\da-fA-F]{1,6}[\x20\t\r\n\f]?|\\[^\r\n\f]|[\w-]|[^\0-\x7f])+)/,TAG:/^((?:\\[\da-fA-F]{1,6}[\x20\t\r\n\f]?|\\[^\r\n\f]|[\w-]|[^\0-\x7f])+|[*])/,ATTR:/^\[[\x20\t\r\n\f]*((?:\\[\da-fA-F]{1,6}[\x20\t\r\n\f]?|\\[^\r\n\f]|[\w-]|[^\0-\x7f])+)(?:[\x20\t\r\n\f]*([*^$|!~]?=)[\x20\t\r\n\f]*(?:'((?:\\.|[^\\'])*)'|"((?:\\.|[^\\"])*)"|((?:\\[\da-fA-F]{1,6}[\x20\t\r\n\f]?|\\[^\r\n\f]|[\w-]|[^\0-\x7f])+))|)[\x20\t\r\n\f]*\]/,PSEUDO:/^:((?:\\[\da-fA-F]{1,6}[\x20\t\r\n\f]?|\\[^\r\n\f]|[\w-]|[^\0-\x7f])+)(?:\((('((?:\\.|[^\\'])*)'|"((?:\\.|[^\\"])*)")|((?:\\.|[^\\()[\]]|\[[\x20\t\r\n\f]*((?:\\[\da-fA-F]{1,6}[\x20\t\r\n\f]?|\\[^\r\n\f]|[\w-]|[^\0-\x7f])+)(?:[\x20\t\r\n\f]*([*^$|!~]?=)[\x20\t\r\n\f]*(?:'((?:\\.|[^\\'])*)'|"((?:\\.|[^\\"])*)"|((?:\\[\da-fA-F]{1,6}[\x20\t\r\n\f]?|\\[^\r\n\f]|[\w-]|[^\0-\x7f])+))|)[\x20\t\r\n\f]*\])*)|.*)\)|)/,CHILD:/^:(only|first|last|nth|nth-last)-(child|of-type)(?:\([\x20\t\r\n\f]*(even|odd|(([+-]|)(\d*)n|)[\x20\t\r\n\f]*(?:([+-]|)[\x20\t\r\n\f]*(\d+)|))[\x20\t\r\n\f]*\)|)/i,bool:/^(?:checked|selected|async|autofocus|autoplay|controls|defer|disabled|hidden|ismap|loop|multiple|open|readonly|required|scoped)$/i,needsContext:/^[\x20\t\r\n\f]*[>+~]|:(even|odd|eq|gt|lt|nth|first|last)(?:\([\x20\t\r\n\f]*((?:-\d)?\d*)[\x20\t\r\n\f]*\)|)(?=[^-]|$)/i},F=/HTML$/i,z=/^(?:input|select|textarea|button)$/i,X=/^h\d$/i,$=/^[^{]+\{\s*\[native \w/,U=/^(?:#([\w-]+)|(\w+)|\.([\w-]+))$/,V=/[+~]/,Y=/\\[\da-fA-F]{1,6}[\x20\t\r\n\f]?|\\([^\r\n\f])/g,Q=function(a,e){var t=String.fromCharCode,o="0x"+a.slice(1)-65536;return e||(0>o?t(o+65536):t(55296|o>>10,56320|1023&o))},K=/([\0-\x1f\x7f]|^-?\d)|^-$|[^\0-\x1f\x7f-\uFFFF\w-]/g,J=function(n,e){return e?"\0"===n?"\uFFFD":n.slice(0,-1)+"\\"+n.charCodeAt(n.length-1).toString(16)+" ":"\\"+n},Z=function(){De()},ee=be(function(t){return!0===t.disabled&&"fieldset"===t.nodeName.toLowerCase()},{dir:"parentNode",next:"legend"});try{k.apply(t=N.call(h.childNodes),h.childNodes),t[h.childNodes.length].nodeType}catch(n){k={apply:t.length?function(n,e){E.apply(n,N.call(e))}:function(a,e){for(var t=a.length,n=0;a[t++]=e[n++];);a.length=t-1}}}for(Se in Ee=W.support={},n=W.isXML=function(a){var e=a&&a.namespaceURI,t=a&&(a.ownerDocument||a).documentElement;return!F.test(e||t&&t.nodeName||"HTML")},De=W.setDocument=function(r){var e,t,i=r?r.ownerDocument||r:h;return i!=d&&9===i.nodeType&&i.documentElement?(o=(d=i).documentElement,Le=!n(d),h!=d&&(t=d.defaultView)&&t.top!==t&&(t.addEventListener?t.addEventListener("unload",Z,!1):t.attachEvent&&t.attachEvent("onunload",Z)),Ee.scope=ue(function(t){return o.appendChild(t).appendChild(d.createElement("div")),void 0!==t.querySelectorAll&&!t.querySelectorAll(":scope fieldset div").length}),Ee.attributes=ue(function(t){return t.className="i",!t.getAttribute("className")}),Ee.getElementsByTagName=ue(function(t){return t.appendChild(d.createComment("")),!t.getElementsByTagName("*").length}),Ee.getElementsByClassName=$.test(d.getElementsByClassName),Ee.getById=ue(function(t){return o.appendChild(t).id=He,!d.getElementsByName||!d.getElementsByName(He).length}),Ee.getById?(ke.filter.ID=function(n){var a=n.replace(Y,Q);return function(t){return t.getAttribute("id")===a}},ke.find.ID=function(a,e){if(void 0!==e.getElementById&&Le){var t=e.getElementById(a);return t?[t]:[]}}):(ke.filter.ID=function(n){var a=n.replace(Y,Q);return function(t){var e=void 0!==t.getAttributeNode&&t.getAttributeNode("id");return e&&e.value===a}},ke.find.ID=function(a,e){if(void 0!==e.getElementById&&Le){var t,n,s,i=e.getElementById(a);if(i){if((t=i.getAttributeNode("id"))&&t.value===a)return[i];for(s=e.getElementsByName(a),n=0;i=s[n++];)if((t=i.getAttributeNode("id"))&&t.value===a)return[i]}return[]}}),ke.find.TAG=Ee.getElementsByTagName?function(n,e){return void 0===e.getElementsByTagName?Ee.qsa?e.querySelectorAll(n):void 0:e.getElementsByTagName(n)}:function(a,e){var t,n=[],s=0,i=e.getElementsByTagName(a);if("*"===a){for(;t=i[s++];)1===t.nodeType&&n.push(t);return n}return i},ke.find.CLASS=Ee.getElementsByClassName&&function(n,e){if(void 0!==e.getElementsByClassName&&Le)return e.getElementsByClassName(n)},s=[],p=[],(Ee.qsa=$.test(d.querySelectorAll))&&(ue(function(n){var e;o.appendChild(n).innerHTML="<a id='"+He+"'></a><select id='"+He+"-\r\\' msallowcapture=''><option selected=''></option></select>",n.querySelectorAll("[msallowcapture^='']").length&&p.push("[*^$]=[\\x20\\t\\r\\n\\f]*(?:''|\"\")"),n.querySelectorAll("[selected]").length||p.push("\\[[\\x20\\t\\r\\n\\f]*(?:value|"+j+")"),n.querySelectorAll("[id~="+He+"-]").length||p.push("~="),(e=d.createElement("input")).setAttribute("name",""),n.appendChild(e),n.querySelectorAll("[name='']").length||p.push("\\[[\\x20\\t\\r\\n\\f]*name[\\x20\\t\\r\\n\\f]*=[\\x20\\t\\r\\n\\f]*(?:''|\"\")"),n.querySelectorAll(":checked").length||p.push(":checked"),n.querySelectorAll("a#"+He+"+*").length||p.push(".#.+[+~]"),n.querySelectorAll("\\\f"),p.push("[\\r\\n\\f]")}),ue(function(n){n.innerHTML="<a href='' disabled='disabled'></a><select disabled='disabled'><option/></select>";var e=d.createElement("input");e.setAttribute("type","hidden"),n.appendChild(e).setAttribute("name","D"),n.querySelectorAll("[name=d]").length&&p.push("name[\\x20\\t\\r\\n\\f]*[*^$|!~]?="),2!==n.querySelectorAll(":enabled").length&&p.push(":enabled",":disabled"),o.appendChild(n).disabled=!0,2!==n.querySelectorAll(":disabled").length&&p.push(":enabled",":disabled"),n.querySelectorAll("*,:x"),p.push(",.*:")})),(Ee.matchesSelector=$.test(u=o.matches||o.webkitMatchesSelector||o.mozMatchesSelector||o.oMatchesSelector||o.msMatchesSelector))&&ue(function(t){Ee.disconnectedMatch=u.call(t,"*"),u.call(t,"[s!='']:x"),s.push("!=",":("+L+")(?:\\((('((?:\\\\.|[^\\\\'])*)'|\"((?:\\\\.|[^\\\\\"])*)\")|((?:\\\\.|[^\\\\()[\\]]|"+("\\[[\\x20\\t\\r\\n\\f]*("+L+")(?:"+D+"*([*^$|!~]?=)"+D+"*(?:'((?:\\\\.|[^\\\\'])*)'|\"((?:\\\\.|[^\\\\\"])*)\"|("+L+"))|)"+D+"*\\]")+")*)|.*)\\)|)")}),p=p.length&&new RegExp(p.join("|")),s=s.length&&new RegExp(s.join("|")),e=$.test(o.compareDocumentPosition),qe=e||$.test(o.contains)?function(a,e){var t=9===a.nodeType?a.documentElement:a,n=e&&e.parentNode;return a===n||n&&1===n.nodeType&&(t.contains?t.contains(n):a.compareDocumentPosition&&16&a.compareDocumentPosition(n))}:function(n,e){if(e)for(;e=e.parentNode;)if(e===n)return!0;return!1},C=e?function(n,e){if(n===e)return c=!0,0;var t=!n.compareDocumentPosition-!e.compareDocumentPosition;return t||(1&(t=(n.ownerDocument||n)==(e.ownerDocument||e)?n.compareDocumentPosition(e):1)||!Ee.sortDetached&&e.compareDocumentPosition(n)===t?n==d||n.ownerDocument==h&&qe(h,n)?-1:e==d||e.ownerDocument==h&&qe(h,e)?1:l?A(l,n)-A(l,e):0:4&t?-1:1)}:function(p,e){if(p===e)return c=!0,0;var t,n=0,r=p.parentNode,u=e.parentNode,g=[p],a=[e];if(!r||!u)return p==d?-1:e==d?1:r?-1:u?1:l?A(l,p)-A(l,e):0;if(r===u)return fe(p,e);for(t=p;t=t.parentNode;)g.unshift(t);for(t=e;t=t.parentNode;)a.unshift(t);for(;g[n]===a[n];)n++;return n?fe(g[n],a[n]):g[n]==h?-1:a[n]==h?1:0},d):d},W.matches=function(n,e){return W(n,null,null,e)},W.matchesSelector=function(n,e){if(De(n),Ee.matchesSelector&&Le&&!T[e+" "]&&(!s||!s.test(e))&&(!p||!p.test(e)))try{var t=u.call(n,e);if(t||Ee.disconnectedMatch||n.document&&11!==n.document.nodeType)return t}catch(t){T(e,!0)}return 0<W(e,d,null,[n]).length},W.contains=function(n,e){return(n.ownerDocument||n)!=d&&De(n),qe(n,e)},W.attr=function(n,e){(n.ownerDocument||n)!=d&&De(n);var t=ke.attrHandle[e.toLowerCase()],a=t&&w.call(ke.attrHandle,e.toLowerCase())?t(n,e,!Le):void 0;return void 0===a?Ee.attributes||!Le?n.getAttribute(e):(a=n.getAttributeNode(e))&&a.specified?a.value:null:a},W.escape=function(t){return(t+"").replace(K,J)},W.error=function(t){throw new Error("Syntax error, unrecognized expression: "+t)},W.uniqueSort=function(n){var e,t=[],a=0,s=0;if(c=!Ee.detectDuplicates,l=!Ee.sortStable&&n.slice(0),n.sort(C),c){for(;e=n[s++];)e===n[s]&&(a=t.push(s));for(;a--;)n.splice(t[a],1)}return l=null,n},Ne=W.getText=function(a){var e,t="",n=0,s=a.nodeType;if(!s)for(;e=a[n++];)t+=Ne(e);else if(1===s||9===s||11===s){if("string"==typeof a.textContent)return a.textContent;for(a=a.firstChild;a;a=a.nextSibling)t+=Ne(a)}else if(3===s||4===s)return a.nodeValue;return t},ke=W.selectors={cacheLength:50,createPseudo:se,match:R,attrHandle:{},find:{},relative:{">":{dir:"parentNode",first:!0}," ":{dir:"parentNode"},"+":{dir:"previousSibling",first:!0},"~":{dir:"previousSibling"}},preFilter:{ATTR:function(t){return t[1]=t[1].replace(Y,Q),t[3]=(t[3]||t[4]||t[5]||"").replace(Y,Q),"~="===t[2]&&(t[3]=" "+t[3]+" "),t.slice(0,4)},CHILD:function(t){return t[1]=t[1].toLowerCase(),"nth"===t[1].slice(0,3)?(t[3]||W.error(t[0]),t[4]=+(t[4]?t[5]+(t[6]||1):2*("even"===t[3]||"odd"===t[3])),t[5]=+(t[7]+t[8]||"odd"===t[3])):t[3]&&W.error(t[0]),t},PSEUDO:function(a){var e,t=!a[6]&&a[2];return R.CHILD.test(a[0])?null:(a[3]?a[2]=a[4]||a[5]||"":t&&M.test(t)&&(e=r(t,!0))&&(e=t.indexOf(")",t.length-e)-t.length)&&(a[0]=a[0].slice(0,e),a[2]=t.slice(0,e)),a.slice(0,3))}},filter:{TAG:function(n){var a=n.replace(Y,Q).toLowerCase();return"*"===n?function(){return!0}:function(t){return t.nodeName&&t.nodeName.toLowerCase()===a}},CLASS:function(n){var a=i[n+" "];return a||(a=new RegExp("(^|[\\x20\\t\\r\\n\\f])"+n+"("+D+"|$)"))&&i(n,function(t){return a.test("string"==typeof t.className&&t.className||void 0!==t.getAttribute&&t.getAttribute("class")||"")})},ATTR:function(a,e,o){return function(n){var s=W.attr(n,a);return null==s?"!="===e:!e||(s+="","="===e?s===o:"!="===e?s!==o:"^="===e?o&&0===s.indexOf(o):"*="===e?o&&-1<s.indexOf(o):"$="===e?o&&s.slice(-o.length)===o:"~="===e?-1<(" "+s.replace(q," ")+" ").indexOf(o):"|="==e&&(s===o||s.slice(0,o.length+1)===o+"-"))}},CHILD:function(u,e,t,n,r){var i="nth"!==u.slice(0,3),o="last"!==u.slice(-4),a="of-type"===e;return 1===n&&0===r?function(t){return!!t.parentNode}:function(e,t,x){var T,l,c,f,d,p,C=i==o?"previousSibling":"nextSibling",g=e.parentNode,m=a&&e.nodeName.toLowerCase(),v=!x&&!a,y=!1;if(g){if(i){for(;C;){for(f=e;f=f[C];)if(a?f.nodeName.toLowerCase()===m:1===f.nodeType)return!1;p=C="only"===u&&!p&&"nextSibling"}return!0}if(p=[o?g.firstChild:g.lastChild],o&&v){for(y=(d=(T=(l=(c=(f=g)[He]||(f[He]={}))[f.uniqueID]||(c[f.uniqueID]={}))[u]||[])[0]===Pe&&T[1])&&T[2],f=d&&g.childNodes[d];f=++d&&f&&f[C]||(y=d=0)||p.pop();)if(1===f.nodeType&&++y&&f===e){l[u]=[Pe,d,y];break}}else if(v&&(y=d=(T=(l=(c=(f=e)[He]||(f[He]={}))[f.uniqueID]||(c[f.uniqueID]={}))[u]||[])[0]===Pe&&T[1]),!1===y)for(;(f=++d&&f&&f[C]||(y=d=0)||p.pop())&&((a?f.nodeName.toLowerCase()!==m:1!==f.nodeType)||!++y||(v&&((l=(c=f[He]||(f[He]={}))[f.uniqueID]||(c[f.uniqueID]={}))[u]=[Pe,y]),f!==e)););return(y-=r)==n||0==y%n&&0<=y/n}}},PSEUDO:function(a,s){var t,d=ke.pseudos[a]||ke.setFilters[a.toLowerCase()]||W.error("unsupported pseudo: "+a);return d[He]?d(s):1<d.length?(t=[a,a,"",s],ke.setFilters.hasOwnProperty(a.toLowerCase())?se(function(t,e){for(var n,i=d(t,s),o=i.length;o--;)t[n=A(t,i[o])]=!(e[n]=i[o])}):function(n){return d(n,0,t)}):d}},pseudos:{not:se(function(o){var s=[],t=[],n=a(o.replace(H,"$1"));return n[He]?se(function(r,e,t,d){for(var i,o=n(r,null,d,[]),a=r.length;a--;)(i=o[a])&&(r[a]=!(e[a]=i))}):function(a,e,i){return s[0]=a,n(s,null,i,t),s[0]=null,!t.pop()}}),has:se(function(n){return function(e){return 0<W(n,e).length}}),contains:se(function(n){return n=n.replace(Y,Q),function(e){return-1<(e.textContent||Ne(e)).indexOf(n)}}),lang:se(function(a){return B.test(a||"")||W.error("unsupported lang: "+a),a=a.replace(Y,Q).toLowerCase(),function(e){var t;do if(t=Le?e.lang:e.getAttribute("xml:lang")||e.getAttribute("lang"))return(t=t.toLowerCase())===a||0===t.indexOf(a+"-");while((e=e.parentNode)&&1===e.nodeType);return!1}}),target:function(e){var t=_.location&&_.location.hash;return t&&t.slice(1)===e.id},root:function(t){return t===o},focus:function(t){return t===d.activeElement&&(!d.hasFocus||d.hasFocus())&&!!(t.type||t.href||~t.tabIndex)},enabled:he(!1),disabled:he(!0),checked:function(n){var e=n.nodeName.toLowerCase();return"input"===e&&!!n.checked||"option"===e&&!!n.selected},selected:function(t){return t.parentNode&&t.parentNode.selectedIndex,!0===t.selected},empty:function(t){for(t=t.firstChild;t;t=t.nextSibling)if(6>t.nodeType)return!1;return!0},parent:function(t){return!ke.pseudos.empty(t)},header:function(t){return X.test(t.nodeName)},input:function(t){return z.test(t.nodeName)},button:function(n){var e=n.nodeName.toLowerCase();return"input"===e&&"button"===n.type||"button"===e},text:function(n){var e;return"input"===n.nodeName.toLowerCase()&&"text"===n.type&&(null==(e=n.getAttribute("type"))||"text"===e.toLowerCase())},first:ge(function(){return[0]}),last:ge(function(n,e){return[e-1]}),eq:ge(function(a,e,t){return[0>t?t+e:t]}),even:ge(function(a,e){for(var t=0;t<e;t+=2)a.push(t);return a}),odd:ge(function(a,e){for(var t=1;t<e;t+=2)a.push(t);return a}),lt:ge(function(a,e,t){for(var n=0>t?t+e:t>e?e:t;0<=--n;)a.push(n);return a}),gt:ge(function(a,e,t){for(var n=0>t?t+e:t;++n<e;)a.push(n);return a})}},ke.pseudos.nth=ke.pseudos.eq,{radio:!0,checkbox:!0,file:!0,password:!0,image:!0})ke.pseudos[Se]=de(Se);for(Se in{submit:!0,reset:!0})ke.pseudos[Se]=pe(Se);return ve.prototype=ke.filters=ke.pseudos,ke.setFilters=new ve,r=W.tokenize=function(r,e){var t,d,p,o,a,s,u,l=b[r+" "];if(l)return e?0:l.slice(0);for(a=r,s=[],u=ke.preFilter;a;){for(o in t&&!(d=P.exec(a))||(d&&(a=a.slice(d[0].length)||a),s.push(p=[])),t=!1,(d=O.exec(a))&&(t=d.shift(),p.push({value:t,type:d[0].replace(H," ")}),a=a.slice(t.length)),ke.filter)(d=R[o].exec(a))&&(!u[o]||(d=u[o](d)))&&(t=d.shift(),p.push({value:t,type:o,matches:d}),a=a.slice(t.length));if(!t)break}return e?a.length:a?W.error(r):b(r,s).slice(0)},a=W.compile=function(a,e){var t,n=[],i=[],o=x[a+" "];if(!o){for(e||(e=r(a)),t=e.length;t--;)(o=Ce(e[t]))[He]?n.push(o):i.push(o);o=x(a,function(r,e){var t=0<e.length,n=0<r.length,a=function(i,l,a,s,p){var c,u,h,f=0,v="0",y=i&&[],b=[],x=je,T=i||n&&ke.find.TAG("*",p),C=Pe+=null==x?1:Math.random()||.1,w=T.length;for(p&&(je=l==d||l||p);v!==w&&null!=(c=T[v]);v++){if(n&&c){for(u=0,l||c.ownerDocument==d||(De(c),a=!Le);h=r[u++];)if(h(c,l||d,a)){s.push(c);break}p&&(Pe=C)}t&&((c=!h&&c)&&f--,i&&y.push(c))}if(f+=v,t&&v!==f){for(u=0;h=e[u++];)h(y,b,l,a);if(i){if(0<f)for(;v--;)y[v]||b[v]||(b[v]=S.call(s));b=we(b)}k.apply(s,b),p&&!i&&0<b.length&&1<f+e.length&&W.uniqueSort(s)}return p&&(Pe=C,je=x),y};return t?se(a):a}(i,n)),o.selector=a}return o},Ae=W.select=function(s,h,m,n){var y,o,u,l,c,f="function"==typeof s&&s,d=!n&&r(s=f.selector||s);if(m=m||[],1===d.length){if(2<(o=d[0]=d[0].slice(0)).length&&"ID"===(u=o[0]).type&&9===h.nodeType&&Le&&ke.relative[o[1].type]){if(!(h=(ke.find.ID(u.matches[0].replace(Y,Q),h)||[])[0]))return m;f&&(h=h.parentNode),s=s.slice(o.shift().value.length)}for(y=R.needsContext.test(s)?0:o.length;y--&&(u=o[y],!ke.relative[l=u.type]);)if((c=ke.find[l])&&(n=c(u.matches[0].replace(Y,Q),V.test(o[0].type)&&me(h.parentNode)||h))){if(o.splice(y,1),!(s=n.length&&ye(o)))return k.apply(m,n),m;break}}return(f||a(s,d))(n,h,!Le,m,!h||V.test(s)&&me(h.parentNode)||h),m},Ee.sortStable=He.split("").sort(C).join("")===He,Ee.detectDuplicates=!!c,De(),Ee.sortDetached=ue(function(t){return 1&t.compareDocumentPosition(d.createElement("fieldset"))}),ue(function(t){return t.innerHTML="<a href='#'></a>","#"===t.firstChild.getAttribute("href")})||ce("type|href|height|width",function(a,e,t){if(!t)return a.getAttribute(e,"type"===e.toLowerCase()?1:2)}),Ee.attributes&&ue(function(t){return t.innerHTML="<input/>",t.firstChild.setAttribute("value",""),""===t.firstChild.getAttribute("value")})||ce("value",function(a,e,t){if(!t&&"input"===a.nodeName.toLowerCase())return a.defaultValue}),ue(function(t){return null==t.getAttribute("disabled")})||ce(j,function(a,e,t){var o;if(!t)return!0===a[e]?e.toLowerCase():(o=a.getAttributeNode(e))&&o.specified?o.value:null}),W}(Zt);ln.find=f,ln.expr=f.selectors,ln.expr[":"]=ln.expr.pseudos,ln.uniqueSort=ln.unique=f.uniqueSort,ln.text=f.getText,ln.isXMLDoc=f.isXML,ln.contains=f.contains,ln.escapeSelector=f.escape;var b=function(a,e,t){for(var n=[];(a=a[e])&&9!==a.nodeType;)if(1===a.nodeType){if(void 0!==t&&ln(a).is(t))break;n.push(a)}return n},x=function(a,e){for(var t=[];a;a=a.nextSibling)1===a.nodeType&&a!==e&&t.push(a);return t},k=ln.expr.match.needsContext,N=/^<([a-z][^\/\0>:\x20\t\r\n\f]*)[\x20\t\r\n\f]*\/?>(?:<\/\1>|)$/i;ln.filter=function(a,e,t){var n=e[0];return t&&(a=":not("+a+")"),1===e.length&&1===n.nodeType?ln.find.matchesSelector(n,a)?[n]:[]:ln.find.matches(a,ln.grep(e,function(t){return 1===t.nodeType}))},ln.fn.extend({find:function(a){var o,t,n=this.length,s=this;if("string"!=typeof a)return this.pushStack(ln(a).filter(function(){for(o=0;o<n;o++)if(ln.contains(s[o],this))return!0}));for(t=this.pushStack([]),o=0;o<n;o++)ln.find(a,s[o],t);return 1<n?ln.uniqueSort(t):t},filter:function(t){return this.pushStack(r(this,t||[],!1))},not:function(t){return this.pushStack(r(this,t||[],!0))},is:function(t){return!!r(this,"string"==typeof t&&k.test(t)?ln(t):t||[],!1).length}});var A,j=/^(?:\s*(<[\w\W]+>)[^>]*|#([\w-]+))$/;(ln.fn.init=function(a,o,s){var n,r;if(!a)return this;if(s=s||A,"string"==typeof a){if(!(n="<"===a[0]&&">"===a[a.length-1]&&3<=a.length?[null,a,null]:j.exec(a))||!n[1]&&o)return!o||o.jquery?(o||s).find(a):this.constructor(o).find(a);if(n[1]){if(o=o instanceof ln?o[0]:o,ln.merge(this,ln.parseHTML(n[1],o&&o.nodeType?o.ownerDocument||o:y,!0)),N.test(n[1])&&ln.isPlainObject(o))for(n in o)dn(this[n])?this[n](o[n]):this.attr(n,o[n]);return this}return(r=y.getElementById(n[2]))&&(this[0]=r,this.length=1),this}return a.nodeType?(this[0]=a,this.length=1,this):dn(a)?void 0===s.ready?a(ln):s.ready(a):ln.makeArray(a,this)}).prototype=ln.fn,A=ln(y);var L=/^(?:parents|prev(?:Until|All))/,H={children:!0,contents:!0,next:!0,prev:!0};ln.fn.extend({has:function(a){var o=ln(a,this),t=o.length;return this.filter(function(){for(var n=0;n<t;n++)if(ln.contains(this,o[n]))return!0})},closest:function(s,d){var t,n=0,r=this.length,i=[],o="string"!=typeof s&&ln(s);if(!k.test(s))for(;n<r;n++)for(t=this[n];t&&t!==d;t=t.parentNode)if(11>t.nodeType&&(o?-1<o.index(t):1===t.nodeType&&ln.find.matchesSelector(t,s))){i.push(t);break}return this.pushStack(1<i.length?ln.uniqueSort(i):i)},index:function(t){return t?"string"==typeof t?a.call(ln(t),this[0]):a.call(this,t.jquery?t[0]:t):this[0]&&this[0].parentNode?this.first().prevAll().length:-1},add:function(n,e){return this.pushStack(ln.uniqueSort(ln.merge(this.get(),ln(n,e))))},addBack:function(t){return this.add(null==t?this.prevObject:this.prevObject.filter(t))}}),ln.each({parent:function(n){var e=n.parentNode;return e&&11!==e.nodeType?e:null},parents:function(t){return b(t,"parentNode")},parentsUntil:function(a,e,t){return b(a,"parentNode",t)},next:function(t){return D(t,"nextSibling")},prev:function(t){return D(t,"previousSibling")},nextAll:function(t){return b(t,"nextSibling")},prevAll:function(t){return b(t,"previousSibling")},nextUntil:function(a,e,t){return b(a,"nextSibling",t)},prevUntil:function(a,e,t){return b(a,"previousSibling",t)},siblings:function(t){return x((t.parentNode||{}).firstChild,t)},children:function(t){return x(t.firstChild)},contents:function(t){return null!=t.contentDocument&&o(t.contentDocument)?t.contentDocument:(S(t,"template")&&(t=t.content||t),ln.merge([],t.childNodes))}},function(a,e){ln.fn[a]=function(t,n){var o=ln.map(this,e,t);return"Until"!==a.slice(-5)&&(n=t),n&&"string"==typeof n&&(o=ln.filter(n,o)),1<this.length&&(H[a]||ln.uniqueSort(o),L.test(a)&&o.reverse()),this.pushStack(o)}});var P=/[^\x20\t\r\n\f]+/g;ln.Callbacks=function(d){d="string"==typeof d?function(n){var a={};return ln.each(n.match(P)||[],function(t,e){a[e]=!0}),a}(d):ln.extend({},d);var p,c,n,h,g=[],f=[],a=-1,s=function(){for(h=h||d.once,n=p=!0;f.length;a=-1)for(c=f.shift();++a<g.length;)!1===g[a].apply(c[0],c[1])&&d.stopOnFalse&&(a=g.length,c=!1);d.memory||(c=!1),p=!1,h&&(g=c?[]:"")},u={add:function(){return g&&(c&&!p&&(a=g.length-1,f.push(c)),function e(t){ln.each(t,function(t,n){dn(n)?d.unique&&u.has(n)||g.push(n):n&&n.length&&"string"!==w(n)&&e(n)})}(arguments),c&&!p&&s()),this},remove:function(){return ln.each(arguments,function(o,e){for(var t;-1<(t=ln.inArray(e,g,t));)g.splice(t,1),t<=a&&a--}),this},has:function(t){return t?-1<ln.inArray(t,g):0<g.length},empty:function(){return g&&(g=[]),this},disable:function(){return h=f=[],g=c="",this},disabled:function(){return!g},lock:function(){return h=f=[],c||p||(g=c=""),this},locked:function(){return!!h},fireWith:function(t,e){return h||(e=[t,(e=e||[]).slice?e.slice():e],f.push(e),p||s()),this},fire:function(){return u.fireWith(this,arguments),this},fired:function(){return!!n}};return u},ln.extend({Deferred:function(a){var d=[["notify","progress",ln.Callbacks("memory"),ln.Callbacks("memory"),2],["resolve","done",ln.Callbacks("once memory"),ln.Callbacks("once memory"),0,"resolved"],["reject","fail",ln.Callbacks("once memory"),ln.Callbacks("once memory"),1,"rejected"]],e="pending",t={state:function(){return e},always:function(){return l.done(arguments).fail(arguments),this},catch:function(n){return t.then(null,n)},pipe:function(){var a=arguments;return ln.Deferred(function(t){ln.each(d,function(e,n){var o=dn(a[n[4]])&&a[n[4]];l[n[1]](function(){var a=o&&o.apply(this,arguments);a&&dn(a.promise)?a.promise().progress(t.notify).done(t.resolve).fail(t.reject):t[n[0]+"With"](this,o?[a]:arguments)})}),a=null}).promise()},then:function(t,e,n){function p(o,e,t,n){return function(){var i=this,s=arguments,r=function(){var d,c;if(!(o<a)){if((d=t.apply(i,s))===e.promise())throw new TypeError("Thenable self-resolution");c=d&&("object"==typeof d||"function"==typeof d)&&d.then,dn(c)?n?c.call(d,p(a,e,q,n),p(a,e,I,n)):(a++,c.call(d,p(a,e,q,n),p(a,e,I,n),p(a,e,q,e.notifyWith))):(t!==q&&(i=void 0,s=[d]),(n||e.resolveWith)(i,s))}},d=n?r:function(){try{r()}catch(n){ln.Deferred.exceptionHook&&ln.Deferred.exceptionHook(n,d.stackTrace),o+1>=a&&(t!==I&&(i=void 0,s=[n]),e.rejectWith(i,s))}};o?d():(ln.Deferred.getStackHook&&(d.stackTrace=ln.Deferred.getStackHook()),Zt.setTimeout(d))}}var a=0;return ln.Deferred(function(a){d[0][3].add(p(0,a,dn(n)?n:q,a.notifyWith)),d[1][3].add(p(0,a,dn(t)?t:q)),d[2][3].add(p(0,a,dn(e)?e:I))}).promise()},promise:function(n){return null==n?t:ln.extend(n,t)}},l={};return ln.each(d,function(n,o){var i=o[2],a=o[5];t[o[1]]=i.add,a&&i.add(function(){e=a},d[3-n][2].disable,d[3-n][3].disable,d[0][2].lock,d[0][3].lock),i.add(o[3].fire),l[o[0]]=function(){return l[o[0]+"With"](this===l?void 0:this,arguments),this},l[o[0]+"With"]=i.fireWith}),t.promise(l),a&&a.call(l,l),l},when:function(s){var d=arguments.length,e=d,l=Array(e),r=an.call(arguments),i=ln.Deferred(),n=function(t){return function(e){l[t]=this,r[t]=1<arguments.length?an.call(arguments):e,--d||i.resolveWith(l,r)}};if(1>=d&&(_(s,i.done(n(e)).resolve,i.reject,!d),"pending"===i.state()||dn(r[e]&&r[e].then)))return i.then();for(;e--;)_(r[e],n(e),i.reject);return i.promise()}});var O=/^(Eval|Internal|Range|Reference|Syntax|Type|URI)Error$/;ln.Deferred.exceptionHook=function(n,e){Zt.console&&Zt.console.warn&&n&&O.test(n.name)&&Zt.console.warn("jQuery.Deferred exception: "+n.message,n.stack,e)},ln.readyException=function(t){Zt.setTimeout(function(){throw t})};var M=ln.Deferred();ln.fn.ready=function(t){return M.then(t).catch(function(t){ln.readyException(t)}),this},ln.extend({isReady:!1,readyWait:1,ready:function(t){(!0===t?--ln.readyWait:ln.isReady)||(ln.isReady=!0,!0!==t&&0<--ln.readyWait||M.resolveWith(y,[ln]))}}),ln.ready.then=M.then,"complete"!==y.readyState&&("loading"===y.readyState||y.documentElement.doScroll)?(y.addEventListener("DOMContentLoaded",W),Zt.addEventListener("load",W)):Zt.setTimeout(ln.ready);var B=function(d,e,t,n,r,i,o){var a=0,s=d.length,p=null==t;if("object"===w(t))for(a in r=!0,t)B(d,e,a,t[a],!0,i,o);else if(void 0!==n&&(r=!0,dn(n)||(o=!0),p&&(o?(e.call(d,n),e=null):(p=e,e=function(a,e,t){return p.call(ln(a),t)})),e))for(;a<s;a++)e(d[a],t,o?n:n.call(d[a],a,e(d[a],t)));return r?d:p?e.call(d):s?e(d[0],t):i},R=/^-ms-/,X=/-([a-z])/g,$=function(t){return 1===t.nodeType||9===t.nodeType||!+t.nodeType};Y.uid=1,Y.prototype={cache:function(n){var e=n[this.expando];return e||(e={},$(n)&&(n.nodeType?n[this.expando]=e:Object.defineProperty(n,this.expando,{value:e,configurable:!0}))),e},set:function(a,e,o){var n,s=this.cache(a);if("string"==typeof e)s[z(e)]=o;else for(n in e)s[z(n)]=e[n];return s},get:function(n,e){return void 0===e?this.cache(n):n[this.expando]&&n[this.expando][z(e)]},access:function(a,e,o){return void 0===e||e&&"string"==typeof e&&void 0===o?this.get(a,e):(this.set(a,e,o),void 0===o?e:o)},remove:function(a,e){var t,n=a[this.expando];if(void 0!==n){if(void 0!==e)for(t=(e=Array.isArray(e)?e.map(z):((e=z(e))in n)?[e]:e.match(P)||[]).length;t--;)delete n[e[t]];(void 0===e||ln.isEmptyObject(n))&&(a.nodeType?a[this.expando]=void 0:delete a[this.expando])}},hasData:function(n){var e=n[this.expando];return void 0!==e&&!ln.isEmptyObject(e)}};var U=new Y,V=new Y,Q=/^(?:\{[\w\W]*\}|\[[\w\W]*\])$/,K=/[A-Z]/g;ln.extend({hasData:function(t){return V.hasData(t)||U.hasData(t)},data:function(a,e,t){return V.access(a,e,t)},removeData:function(n,e){V.remove(n,e)},_data:function(a,e,t){return U.access(a,e,t)},_removeData:function(n,e){U.remove(n,e)}}),ln.fn.extend({data:function(s,d){var t,n,r,i=this[0],o=i&&i.attributes;if(void 0===s){if(this.length&&(r=V.get(i),1===i.nodeType&&!U.get(i,"hasDataAttrs"))){for(t=o.length;t--;)o[t]&&0===(n=o[t].name).indexOf("data-")&&(n=z(n.slice(5)),G(i,n,r[n]));U.set(i,"hasDataAttrs",!0)}return r}return"object"==typeof s?this.each(function(){V.set(this,s)}):B(this,function(e){var t;return i&&void 0===e?void 0!==(t=V.get(i,s))||void 0!==(t=G(i,s))?t:void 0:void this.each(function(){V.set(this,s,e)})},null,d,1<arguments.length,null,!0)},removeData:function(t){return this.each(function(){V.remove(this,t)})}}),ln.extend({queue:function(a,e,t){var n;if(a)return e=(e||"fx")+"queue",n=U.get(a,e),t&&(!n||Array.isArray(t)?n=U.access(a,e,ln.makeArray(t)):n.push(t)),n||[]},dequeue:function(a,e){e=e||"fx";var t=ln.queue(a,e),n=t.length,s=t.shift(),i=ln._queueHooks(a,e);"inprogress"===s&&(s=t.shift(),n--),s&&("fx"===e&&t.unshift("inprogress"),delete i.stop,s.call(a,function(){ln.dequeue(a,e)},i)),!n&&i&&i.empty.fire()},_queueHooks:function(a,e){var t=e+"queueHooks";return U.get(a,t)||U.access(a,t,{empty:ln.Callbacks("once memory").add(function(){U.remove(a,[e+"queue",t])})})}}),ln.fn.extend({queue:function(a,o){var t=2;return"string"!=typeof a&&(o=a,a="fx",t--),arguments.length<t?ln.queue(this[0],a):void 0===o?this:this.each(function(){var e=ln.queue(this,a,o);ln._queueHooks(this,a),"fx"===a&&"inprogress"!==e[0]&&ln.dequeue(this,a)})},dequeue:function(t){return this.each(function(){ln.dequeue(this,t)})},clearQueue:function(t){return this.queue(t||"fx",[])},promise:function(d,l){var t,n=1,r=ln.Deferred(),i=this,o=this.length,a=function(){--n||r.resolveWith(i,[i])};for("string"!=typeof d&&(l=d,d=void 0),d=d||"fx";o--;)(t=U.get(i[o],d+"queueHooks"))&&t.empty&&(n++,t.empty.add(a));return a(),r.promise(l)}});var Z=/[+-]?(?:\d*\.|)\d+(?:[eE][+-]?\d+|)/.source,ee=new RegExp("^(?:([+-])=|)("+Z+")([a-z%]*)$","i"),te=["Top","Right","Bottom","Left"],oe=y.documentElement,ae=function(t){return ln.contains(t.ownerDocument,t)},se={composed:!0};oe.getRootNode&&(ae=function(t){return ln.contains(t.ownerDocument,t)||t.getRootNode(se)===t.ownerDocument});var ie=function(n,e){return"none"===(n=e||n).style.display||""===n.style.display&&ae(n)&&"none"===ln.css(n,"display")},re={};ln.fn.extend({show:function(){return de(this,!0)},hide:function(){return de(this)},toggle:function(t){return"boolean"==typeof t?t?this.show():this.hide():this.each(function(){ie(this)?ln(this).show():ln(this).hide()})}});var le,ue,he=/^(?:checkbox|radio)$/i,ge=/<([a-z][^\/\0>\x20\t\r\n\f]*)/i,fe=/^$|^module$|\/(?:java|ecma)script/i;le=y.createDocumentFragment().appendChild(y.createElement("div")),(ue=y.createElement("input")).setAttribute("type","radio"),ue.setAttribute("checked","checked"),ue.setAttribute("name","t"),le.appendChild(ue),rn.checkClone=le.cloneNode(!0).cloneNode(!0).lastChild.checked,le.innerHTML="<textarea>x</textarea>",rn.noCloneChecked=!!le.cloneNode(!0).lastChild.defaultValue,le.innerHTML="<option></option>",rn.option=!!le.lastChild;var me={thead:[1,"<table>","</table>"],col:[2,"<table><colgroup>","</colgroup></table>"],tr:[2,"<table><tbody>","</tbody></table>"],td:[3,"<table><tbody><tr>","</tr></tbody></table>"],_default:[0,"",""]};me.tbody=me.tfoot=me.colgroup=me.caption=me.thead,me.th=me.td,rn.option||(me.optgroup=me.option=[1,"<select multiple='multiple'>","</select>"]);var ye=/<|&#?\w+;/,be=/^([^.]*)(?:\.(.+)|)/;ln.event={global:{},add:function(y,e,t,b,x){var v,o,a,s,u,l,c,f,d,T,h,C=U.get(y);if($(y))for(t.handler&&(t=(v=t).handler,x=v.selector),x&&ln.find.matchesSelector(oe,x),t.guid||(t.guid=ln.guid++),(s=C.events)||(s=C.events=Object.create(null)),(o=C.handle)||(o=C.handle=function(e){return void 0!==ln&&ln.event.triggered!==e.type?ln.event.dispatch.apply(y,arguments):void 0}),u=(e=(e||"").match(P)||[""]).length;u--;)d=h=(a=be.exec(e[u])||[])[1],T=(a[2]||"").split(".").sort(),d&&(c=ln.event.special[d]||{},d=(x?c.delegateType:c.bindType)||d,c=ln.event.special[d]||{},l=ln.extend({type:d,origType:h,data:b,handler:t,guid:t.guid,selector:x,needsContext:x&&ln.expr.match.needsContext.test(x),namespace:T.join(".")},v),(f=s[d])||((f=s[d]=[]).delegateCount=0,c.setup&&!1!==c.setup.call(y,b,T,o)||y.addEventListener&&y.addEventListener(d,o)),c.add&&(c.add.call(y,l),l.handler.guid||(l.handler.guid=t.guid)),x?f.splice(f.delegateCount++,0,l):f.push(l),ln.event.global[d]=!0)},remove:function(y,e,t,n,r){var b,o,a,s,u,l,c,f,d,p,h,g=U.hasData(y)&&U.get(y);if(g&&(s=g.events)){for(u=(e=(e||"").match(P)||[""]).length;u--;)if(d=h=(a=be.exec(e[u])||[])[1],p=(a[2]||"").split(".").sort(),d){for(c=ln.event.special[d]||{},f=s[d=(n?c.delegateType:c.bindType)||d]||[],a=a[2]&&new RegExp("(^|\\.)"+p.join("\\.(?:.*\\.|)")+"(\\.|$)"),o=b=f.length;b--;)l=f[b],!r&&h!==l.origType||t&&t.guid!==l.guid||a&&!a.test(l.namespace)||n&&n!==l.selector&&("**"!==n||!l.selector)||(f.splice(b,1),l.selector&&f.delegateCount--,c.remove&&c.remove.call(y,l));o&&!f.length&&(c.teardown&&!1!==c.teardown.call(y,p,g.handle)||ln.removeEvent(y,d,g.handle),delete s[d])}else for(d in s)ln.event.remove(y,d+e[u],t,n,!0);ln.isEmptyObject(s)&&U.remove(y,"handle events")}},dispatch:function(d){var e,t,n,r,i,o,a=Array(arguments.length),s=ln.event.fix(d),p=(U.get(this,"events")||Object.create(null))[s.type]||[],l=ln.event.special[s.type]||{};for(a[0]=s,e=1;e<arguments.length;e++)a[e]=arguments[e];if(s.delegateTarget=this,!l.preDispatch||!1!==l.preDispatch.call(this,s)){for(o=ln.event.handlers.call(this,s,p),e=0;(r=o[e++])&&!s.isPropagationStopped();)for(s.currentTarget=r.elem,t=0;(i=r.handlers[t++])&&!s.isImmediatePropagationStopped();)s.rnamespace&&!1!==i.namespace&&!s.rnamespace.test(i.namespace)||(s.handleObj=i,s.data=i.data,void 0!==(n=((ln.event.special[i.origType]||{}).handle||i.handler).apply(r.elem,a))&&!1===(s.result=n)&&(s.preventDefault(),s.stopPropagation()));return l.postDispatch&&l.postDispatch.call(this,s),s.result}},handlers:function(d,e){var t,n,r,i,p,a=[],s=e.delegateCount,c=d.target;if(s&&c.nodeType&&!("click"===d.type&&1<=d.button))for(;c!==this;c=c.parentNode||this)if(1===c.nodeType&&("click"!==d.type||!0!==c.disabled)){for(i=[],p={},t=0;t<s;t++)void 0===p[r=(n=e[t]).selector+" "]&&(p[r]=n.needsContext?-1<ln(r,this).index(c):ln.find(r,this,null,[c]).length),p[r]&&i.push(n);i.length&&a.push({elem:c,handlers:i})}return c=this,s<e.length&&a.push({elem:c,handlers:e.slice(s)}),a},addProp:function(n,e){Object.defineProperty(ln.Event.prototype,n,{enumerable:!0,configurable:!0,get:dn(e)?function(){if(this.originalEvent)return e(this.originalEvent)}:function(){if(this.originalEvent)return this.originalEvent[n]},set:function(e){Object.defineProperty(this,n,{enumerable:!0,configurable:!0,writable:!0,value:e})}})},fix:function(t){return t[ln.expando]?t:new ln.Event(t)},special:{load:{noBubble:!0},click:{setup:function(n){var e=this||n;return he.test(e.type)&&e.click&&S(e,"input")&&je(e,"click",Ce),!1},trigger:function(n){var e=this||n;return he.test(e.type)&&e.click&&S(e,"input")&&je(e,"click"),!0},_default:function(n){var e=n.target;return he.test(e.type)&&e.click&&S(e,"input")&&U.get(e,"click")||S(e,"a")}},beforeunload:{postDispatch:function(t){void 0!==t.result&&t.originalEvent&&(t.originalEvent.returnValue=t.result)}}}},ln.removeEvent=function(a,e,t){a.removeEventListener&&a.removeEventListener(e,t)},ln.Event=function(n,e){return this instanceof ln.Event?void(n&&n.type?(this.originalEvent=n,this.type=n.type,this.isDefaultPrevented=n.defaultPrevented||void 0===n.defaultPrevented&&!1===n.returnValue?Ce:we,this.target=n.target&&3===n.target.nodeType?n.target.parentNode:n.target,this.currentTarget=n.currentTarget,this.relatedTarget=n.relatedTarget):this.type=n,e&&ln.extend(this,e),this.timeStamp=n&&n.timeStamp||Date.now(),this[ln.expando]=!0):new ln.Event(n,e)},ln.Event.prototype={constructor:ln.Event,isDefaultPrevented:we,isPropagationStopped:we,isImmediatePropagationStopped:we,isSimulated:!1,preventDefault:function(){var t=this.originalEvent;this.isDefaultPrevented=Ce,t&&!this.isSimulated&&t.preventDefault()},stopPropagation:function(){var t=this.originalEvent;this.isPropagationStopped=Ce,t&&!this.isSimulated&&t.stopPropagation()},stopImmediatePropagation:function(){var t=this.originalEvent;this.isImmediatePropagationStopped=Ce,t&&!this.isSimulated&&t.stopImmediatePropagation(),this.stopPropagation()}},ln.each({altKey:!0,bubbles:!0,cancelable:!0,changedTouches:!0,ctrlKey:!0,detail:!0,eventPhase:!0,metaKey:!0,pageX:!0,pageY:!0,shiftKey:!0,view:!0,char:!0,code:!0,charCode:!0,key:!0,keyCode:!0,button:!0,buttons:!0,clientX:!0,clientY:!0,offsetX:!0,offsetY:!0,pointerId:!0,pointerType:!0,screenX:!0,screenY:!0,targetTouches:!0,toElement:!0,touches:!0,which:!0},ln.event.addProp),ln.each({focus:"focusin",blur:"focusout"},function(n,e){ln.event.special[n]={setup:function(){return je(this,n,Se),!1},trigger:function(){return je(this,n),!0},_default:function(){return!0},delegateType:e}}),ln.each({mouseenter:"mouseover",mouseleave:"mouseout",pointerenter:"pointerover",pointerleave:"pointerout"},function(n,a){ln.event.special[n]={delegateType:a,bindType:a,handle:function(t){var e,n=this,s=t.relatedTarget,i=t.handleObj;return s&&(s===n||ln.contains(n,s))||(t.type=i.origType,e=i.handler.apply(this,arguments),t.type=a),e}}}),ln.fn.extend({on:function(a,e,t,n){return ke(this,a,e,t,n)},one:function(a,e,t,n){return ke(this,a,e,t,n,1)},off:function(a,o,s){var n,r;if(a&&a.preventDefault&&a.handleObj)return n=a.handleObj,ln(a.delegateTarget).off(n.namespace?n.origType+"."+n.namespace:n.origType,n.selector,n.handler),this;if("object"==typeof a){for(r in a)this.off(r,o,a[r]);return this}return!1!==o&&"function"!=typeof o||(s=o,o=void 0),!1===s&&(s=we),this.each(function(){ln.event.remove(this,a,s,o)})}});var ve=/<script|<style|<link/i,Te=/checked\s*(?:[^=]|=\s*.checked.)/i,Ee=/^\s*<!(?:\[CDATA\[|--)|(?:\]\]|--)>\s*$/g;ln.extend({htmlPrefilter:function(t){return t},clone:function(d,e,t){var n,r,i,o,a=d.cloneNode(!0),s=ae(d);if(!(rn.noCloneChecked||1!==d.nodeType&&11!==d.nodeType||ln.isXMLDoc(d)))for(o=pe(a),n=0,r=(i=pe(d)).length;n<r;n++)Re(i[n],o[n]);if(e)if(t)for(i=i||pe(d),o=o||pe(a),n=0,r=i.length;n<r;n++)Pe(i[n],o[n]);else Pe(d,a);return 0<(o=pe(a,"script")).length&&ce(o,!s&&pe(d,"script")),a},cleanData:function(a){for(var e,t,n,s=ln.event.special,i=0;void 0!==(t=a[i]);i++)if($(t)){if(e=t[U.expando]){if(e.events)for(n in e.events)s[n]?ln.event.remove(t,n):ln.removeEvent(t,n,e.handle);t[U.expando]=void 0}t[V.expando]&&(t[V.expando]=void 0)}}}),ln.fn.extend({detach:function(t){return Me(this,t,!0)},remove:function(t){return Me(this,t)},text:function(t){return B(this,function(t){return void 0===t?ln.text(this):this.empty().each(function(){1!==this.nodeType&&11!==this.nodeType&&9!==this.nodeType||(this.textContent=t)})},null,t,arguments.length)},append:function(){return Ie(this,arguments,function(t){1!==this.nodeType&&11!==this.nodeType&&9!==this.nodeType||Ne(this,t).appendChild(t)})},prepend:function(){return Ie(this,arguments,function(n){if(1===this.nodeType||11===this.nodeType||9===this.nodeType){var e=Ne(this,n);e.insertBefore(n,e.firstChild)}})},before:function(){return Ie(this,arguments,function(t){this.parentNode&&this.parentNode.insertBefore(t,this)})},after:function(){return Ie(this,arguments,function(t){this.parentNode&&this.parentNode.insertBefore(t,this.nextSibling)})},empty:function(){for(var n,e=0;null!=(n=this[e]);e++)1===n.nodeType&&(ln.cleanData(pe(n,!1)),n.textContent="");return this},clone:function(n,e){return n=null!=n&&n,e=null==e?n:e,this.map(function(){return ln.clone(this,n,e)})},html:function(t){return B(this,function(a){var o=this[0]||{},t=0,n=this.length;if(void 0===a&&1===o.nodeType)return o.innerHTML;if("string"==typeof a&&!ve.test(a)&&!me[(ge.exec(a)||["",""])[1].toLowerCase()]){a=ln.htmlPrefilter(a);try{for(;t<n;t++)1===(o=this[t]||{}).nodeType&&(ln.cleanData(pe(o,!1)),o.innerHTML=a);o=0}catch(t){}}o&&this.empty().append(a)},null,t,arguments.length)},replaceWith:function(){var a=[];return Ie(this,arguments,function(e){var t=this.parentNode;0>ln.inArray(this,a)&&(ln.cleanData(pe(this)),t&&t.replaceChild(e,this))},a)}}),ln.each({appendTo:"append",prependTo:"prepend",insertBefore:"before",insertAfter:"after",replaceAll:"replaceWith"},function(n,d){ln.fn[n]=function(t){for(var e,n=[],r=ln(t),i=r.length-1,o=0;o<=i;o++)e=o===i?this:this.clone(!0),ln(r[o])[d](e),s.apply(n,e.get());return this.pushStack(n)}});var De=new RegExp("^("+Z+")(?!px)[a-z%]+$","i"),Le=function(n){var e=n.ownerDocument.defaultView;return e&&e.opener||(e=Zt),e.getComputedStyle(n)},qe=function(a,e,t){var n,s,i={};for(s in e)i[s]=a.style[s],a.style[s]=e[s];for(s in n=t.call(a),e)a.style[s]=i[s];return n},Be=new RegExp(te.join("|"),"i");!function(){function r(){if(l){p.style.cssText="position:absolute;left:-11111px;width:60px;margin-top:1px;padding:0;border:0",l.style.cssText="position:relative;display:block;box-sizing:border-box;overflow:scroll;margin:auto;border:1px;padding:1px;width:60%;top:1%",oe.appendChild(p).appendChild(l);var a=Zt.getComputedStyle(l);t="1%"!==a.top,s=12===d(a.marginLeft),l.style.right="60%",o=36===d(a.right),n=36===d(a.width),l.style.position="absolute",i=12===d(l.offsetWidth/3),oe.removeChild(p),l=null}}function d(t){return Math.round(parseFloat(t))}var t,n,i,o,a,s,p=y.createElement("div"),l=y.createElement("div");l.style&&(l.style.backgroundClip="content-box",l.cloneNode(!0).style.backgroundClip="",rn.clearCloneStyle="content-box"===l.style.backgroundClip,ln.extend(rn,{boxSizingReliable:function(){return r(),n},pixelBoxStyles:function(){return r(),o},pixelPosition:function(){return r(),t},reliableMarginLeft:function(){return r(),s},scrollboxSize:function(){return r(),i},reliableTrDimensions:function(){var o,e,t,n;return null==a&&(o=y.createElement("table"),e=y.createElement("tr"),t=y.createElement("div"),o.style.cssText="position:absolute;left:-11111px;border-collapse:separate",e.style.cssText="border:1px solid",e.style.height="1px",t.style.height="9px",t.style.display="block",oe.appendChild(o).appendChild(e).appendChild(t),n=Zt.getComputedStyle(e),a=parseInt(n.height,10)+parseInt(n.borderTopWidth,10)+parseInt(n.borderBottomWidth,10)===e.offsetHeight,oe.removeChild(o)),a}}))}();var We=["Webkit","Moz","ms"],Fe=y.createElement("div").style,Xe={},$e=/^(none|table(?!-c[ea]).+)/,Ve=/^--/,Ge={position:"absolute",visibility:"hidden",display:"block"},Qe={letterSpacing:"0",fontWeight:"400"};ln.extend({cssHooks:{opacity:{get:function(a,e){if(e){var t=_e(a,"opacity");return""===t?"1":t}}}},cssNumber:{animationIterationCount:!0,columnCount:!0,fillOpacity:!0,flexGrow:!0,flexShrink:!0,fontWeight:!0,gridArea:!0,gridColumn:!0,gridColumnEnd:!0,gridColumnStart:!0,gridRow:!0,gridRowEnd:!0,gridRowStart:!0,lineHeight:!0,opacity:!0,order:!0,orphans:!0,widows:!0,zIndex:!0,zoom:!0},cssProps:{},style:function(d,e,t,p){if(d&&3!==d.nodeType&&8!==d.nodeType&&d.style){var r,i,o,a=z(e),s=Ve.test(e),c=d.style;if(s||(e=Ue(a)),o=ln.cssHooks[e]||ln.cssHooks[a],void 0===t)return o&&"get"in o&&void 0!==(r=o.get(d,!1,p))?r:c[e];"string"==(i=typeof t)&&(r=ee.exec(t))&&r[1]&&(t=J(d,e,r),i="number"),null!=t&&t==t&&("number"!==i||s||(t+=r&&r[3]||(ln.cssNumber[a]?"":"px")),rn.clearCloneStyle||""!==t||0!==e.indexOf("background")||(c[e]="inherit"),o&&"set"in o&&void 0===(t=o.set(d,t,p))||(s?c.setProperty(e,t):c[e]=t))}},css:function(d,e,t,n){var r,i,o,a=z(e);return Ve.test(e)||(e=Ue(a)),(o=ln.cssHooks[e]||ln.cssHooks[a])&&"get"in o&&(r=o.get(d,!0,t)),void 0===r&&(r=_e(d,e,n)),"normal"===r&&e in Qe&&(r=Qe[e]),""===t||t?(i=parseFloat(r),!0===t||isFinite(i)?i||0:r):r}}),ln.each(["height","width"],function(n,d){ln.cssHooks[d]={get:function(t,e,n){if(e)return!$e.test(ln.css(t,"display"))||t.getClientRects().length&&t.getBoundingClientRect().width?tt(t,d,n):qe(t,Ge,function(){return tt(t,d,n)})},set:function(t,e,n){var r,i=Le(t),o=!rn.scrollboxSize()&&"absolute"===i.position,a=(o||n)&&"border-box"===ln.css(t,"boxSizing",!1,i),s=n?et(t,d,n,a,i):0;return a&&o&&(s-=$t(t["offset"+d[0].toUpperCase()+d.slice(1)]-parseFloat(i[d])-et(t,d,"border",!1,i)-.5)),s&&(r=ee.exec(e))&&"px"!==(r[3]||"px")&&(t.style[d]=e,e=ln.css(t,d)),Ye(0,e,s)}}}),ln.cssHooks.marginLeft=ze(rn.reliableMarginLeft,function(n,e){if(e)return(parseFloat(_e(n,"marginLeft"))||n.getBoundingClientRect().left-qe(n,{marginLeft:0},function(){return n.getBoundingClientRect().left}))+"px"}),ln.each({margin:"",padding:"",border:"Width"},function(a,e){ln.cssHooks[a+e]={expand:function(t){for(var s=0,r={},i="string"==typeof t?t.split(" "):[t];4>s;s++)r[a+te[s]+e]=i[s]||i[s-2]||i[0];return r}},"margin"!==a&&(ln.cssHooks[a+e].set=Ye)}),ln.fn.extend({css:function(n,e){return B(this,function(s,e,t){var n,r,i={},o=0;if(Array.isArray(e)){for(n=Le(s),r=e.length;o<r;o++)i[e[o]]=ln.css(s,e[o],!1,n);return i}return void 0===t?ln.css(s,e):ln.style(s,e,t)},n,e,1<arguments.length)}}),ln.Tween=nt,nt.prototype={constructor:nt,init:function(a,e,t,n,s,i){this.elem=a,this.prop=t,this.easing=s||ln.easing._default,this.options=e,this.start=this.now=this.cur(),this.end=n,this.unit=i||(ln.cssNumber[t]?"":"px")},cur:function(){var t=nt.propHooks[this.prop];return t&&t.get?t.get(this):nt.propHooks._default.get(this)},run:function(a){var e,t=nt.propHooks[this.prop];return this.pos=this.options.duration?e=ln.easing[this.easing](a,this.options.duration*a,0,1,this.options.duration):e=a,this.now=(this.end-this.start)*e+this.start,this.options.step&&this.options.step.call(this.elem,this.now,this),t&&t.set?t.set(this):nt.propHooks._default.set(this),this}},nt.prototype.init.prototype=nt.prototype,nt.propHooks={_default:{get:function(n){var e;return 1!==n.elem.nodeType||null!=n.elem[n.prop]&&null==n.elem.style[n.prop]?n.elem[n.prop]:(e=ln.css(n.elem,n.prop,""))&&"auto"!==e?e:0},set:function(t){ln.fx.step[t.prop]?ln.fx.step[t.prop](t):1===t.elem.nodeType&&(ln.cssHooks[t.prop]||null!=t.elem.style[Ue(t.prop)])?ln.style(t.elem,t.prop,t.now+t.unit):t.elem[t.prop]=t.now}}},nt.propHooks.scrollTop=nt.propHooks.scrollLeft={set:function(t){t.elem.nodeType&&t.elem.parentNode&&(t.elem[t.prop]=t.now)}},ln.easing={linear:function(t){return t},swing:function(t){return .5-Math.cos(t*Math.PI)/2},_default:"swing"},ln.fx=nt.prototype.init,ln.fx.step={};var Ke,Je,Ze=/^(?:toggle|show|hide)$/,at=/queueHooks$/;ln.Animation=ln.extend(ft,{tweeners:{"*":[function(a,e){var t=this.createTween(a,e);return J(t.elem,a,ee.exec(e),t),t}]},tweener:function(a,e){dn(a)?(e=a,a=["*"]):a=a.match(P);for(var t,n=0,o=a.length;n<o;n++)t=a[n],ft.tweeners[t]=ft.tweeners[t]||[],ft.tweeners[t].unshift(e)},prefilters:[function(y,e,t){var n,r,i,o,a,s,u,b,c="width"in e||"height"in e,f=this,d={},p=y.style,h=y.nodeType&&ie(y),x=U.get(y,"fxshow");for(n in t.queue||(null==(o=ln._queueHooks(y,"fx")).unqueued&&(o.unqueued=0,a=o.empty.fire,o.empty.fire=function(){o.unqueued||a()}),o.unqueued++,f.always(function(){f.always(function(){o.unqueued--,ln.queue(y,"fx").length||o.empty.fire()})})),e)if(r=e[n],Ze.test(r)){if(delete e[n],i=i||"toggle"===r,r===(h?"hide":"show")){if("show"!==r||!x||void 0===x[n])continue;h=!0}d[n]=x&&x[n]||ln.style(y,n)}if((s=!ln.isEmptyObject(e))||!ln.isEmptyObject(d))for(n in c&&1===y.nodeType&&(t.overflow=[p.overflow,p.overflowX,p.overflowY],null==(u=x&&x.display)&&(u=U.get(y,"display")),"none"===(b=ln.css(y,"display"))&&(u?b=u:(de([y],!0),u=y.style.display||u,b=ln.css(y,"display"),de([y]))),("inline"===b||"inline-block"===b&&null!=u)&&"none"===ln.css(y,"float")&&(s||(f.done(function(){p.display=u}),null==u&&(b=p.display,u="none"===b?"":b)),p.display="inline-block")),t.overflow&&(p.overflow="hidden",f.always(function(){p.overflow=t.overflow[0],p.overflowX=t.overflow[1],p.overflowY=t.overflow[2]})),s=!1,d)s||(x?"hidden"in x&&(h=x.hidden):x=U.access(y,"fxshow",{display:u}),i&&(x.hidden=!h),h&&de([y],!0),f.done(function(){for(n in h||de([y]),U.remove(y,"fxshow"),d)ln.style(y,n,d[n])})),s=ct(h?x[n]:0,n,f),n in x||(x[n]=s.start,h&&(s.end=s.start,s.start=0))}],prefilter:function(n,e){e?ft.prefilters.unshift(n):ft.prefilters.push(n)}}),ln.speed=function(a,o,t){var s=a&&"object"==typeof a?ln.extend({},a):{complete:t||!t&&o||dn(a)&&a,duration:a,easing:t&&o||o&&!dn(o)&&o};return ln.fx.off?s.duration=0:"number"!=typeof s.duration&&(s.duration in ln.fx.speeds?s.duration=ln.fx.speeds[s.duration]:s.duration=ln.fx.speeds._default),null!=s.queue&&!0!==s.queue||(s.queue="fx"),s.old=s.complete,s.complete=function(){dn(s.old)&&s.old.call(this),s.queue&&ln.dequeue(this,s.queue)},s},ln.fn.extend({fadeTo:function(a,e,o,n){return this.filter(ie).css("opacity",0).show().end().animate({opacity:e},a,o,n)},animate:function(s,e,t,n){var r=ln.isEmptyObject(s),i=ln.speed(e,t,n),o=function(){var e=ft(this,ln.extend({},s),i);(r||U.get(this,"finish"))&&e.stop(!0)};return o.finish=o,r||!1===i.queue?this.each(o):this.queue(i.queue,o)},stop:function(s,a,d){var n=function(n){var e=n.stop;delete n.stop,e(d)};return"string"!=typeof s&&(d=a,a=s,s=void 0),a&&this.queue(s||"fx",[]),this.each(function(){var e=!0,r=null!=s&&s+"queueHooks",i=ln.timers,o=U.get(this);if(r)o[r]&&o[r].stop&&n(o[r]);else for(r in o)o[r]&&o[r].stop&&at.test(r)&&n(o[r]);for(r=i.length;r--;)i[r].elem!==this||null!=s&&i[r].queue!==s||(i[r].anim.stop(d),e=!1,i.splice(r,1));!e&&d||ln.dequeue(this,s)})},finish:function(s){return!1!==s&&(s=s||"fx"),this.each(function(){var e,t=U.get(this),n=t[s+"queue"],r=t[s+"queueHooks"],i=ln.timers,o=n?n.length:0;for(t.finish=!0,ln.queue(this,s,[]),r&&r.stop&&r.stop.call(this,!0),e=i.length;e--;)i[e].elem===this&&i[e].queue===s&&(i[e].anim.stop(!0),i.splice(e,1));for(e=0;e<o;e++)n[e]&&n[e].finish&&n[e].finish.call(this);delete t.finish})}}),ln.each(["toggle","show","hide"],function(a,o){var t=ln.fn[o];ln.fn[o]=function(n,a,s){return null==n||"boolean"==typeof n?t.apply(this,arguments):this.animate(lt(o,!0),n,a,s)}}),ln.each({slideDown:lt("show"),slideUp:lt("hide"),slideToggle:lt("toggle"),fadeIn:{opacity:"show"},fadeOut:{opacity:"hide"},fadeToggle:{opacity:"toggle"}},function(n,a){ln.fn[n]=function(t,e,n){return this.animate(a,t,e,n)}}),ln.timers=[],ln.fx.tick=function(){var a,e=0,t=ln.timers;for(Ke=Date.now();e<t.length;e++)(a=t[e])()||t[e]!==a||t.splice(e--,1);t.length||ln.fx.stop(),Ke=void 0},ln.fx.timer=function(t){ln.timers.push(t),ln.fx.start()},ln.fx.interval=13,ln.fx.start=function(){Je||(Je=!0,en())},ln.fx.stop=function(){Je=null},ln.fx.speeds={slow:600,fast:200,_default:400},ln.fn.delay=function(a,e){return a=ln.fx&&ln.fx.speeds[a]||a,e=e||"fx",this.queue(e,function(e,t){var n=Zt.setTimeout(e,a);t.stop=function(){Zt.clearTimeout(n)}})},function(){var n=y.createElement("input"),e=y.createElement("select").appendChild(y.createElement("option"));n.type="checkbox",rn.checkOn=""!==n.value,rn.optSelected=e.selected,(n=y.createElement("input")).value="t",n.type="radio",rn.radioValue="t"===n.value}();var ot,st=ln.expr.attrHandle;ln.fn.extend({attr:function(n,e){return B(this,ln.attr,n,e,1<arguments.length)},removeAttr:function(t){return this.each(function(){ln.removeAttr(this,t)})}}),ln.extend({attr:function(a,e,t){var n,s,i=a.nodeType;if(3!==i&&8!==i&&2!==i)return void 0===a.getAttribute?ln.prop(a,e,t):(1===i&&ln.isXMLDoc(a)||(s=ln.attrHooks[e.toLowerCase()]||(ln.expr.match.bool.test(e)?ot:void 0)),void 0===t?s&&"get"in s&&null!==(n=s.get(a,e))?n:null==(n=ln.find.attr(a,e))?void 0:n:null===t?void ln.removeAttr(a,e):s&&"set"in s&&void 0!==(n=s.set(a,t,e))?n:(a.setAttribute(e,t+""),t))},attrHooks:{type:{set:function(a,e){if(!rn.radioValue&&"radio"===e&&S(a,"input")){var t=a.value;return a.setAttribute("type",e),t&&(a.value=t),e}}}},removeAttr:function(a,e){var t,n=0,o=e&&e.match(P);if(o&&1===a.nodeType)for(;t=o[n++];)a.removeAttribute(t)}}),ot={set:function(a,e,t){return!1===e?ln.removeAttr(a,t):a.setAttribute(t,t),t}},ln.each(ln.expr.match.bool.source.match(/\w+/g),function(a,e){var s=st[e]||ln.find.attr;st[e]=function(n,e,t){var r,i,o=e.toLowerCase();return t||(i=st[o],st[o]=r,r=null==s(n,e,t)?null:o,st[o]=i),r}});var it=/^(?:input|select|textarea|button)$/i,pt=/^(?:a|area)$/i;ln.fn.extend({prop:function(n,e){return B(this,ln.prop,n,e,1<arguments.length)},removeProp:function(t){return this.each(function(){delete this[ln.propFix[t]||t]})}}),ln.extend({prop:function(a,e,t){var n,s,i=a.nodeType;if(3!==i&&8!==i&&2!==i)return 1===i&&ln.isXMLDoc(a)||(e=ln.propFix[e]||e,s=ln.propHooks[e]),void 0===t?s&&"get"in s&&null!==(n=s.get(a,e))?n:a[e]:s&&"set"in s&&void 0!==(n=s.set(a,t,e))?n:a[e]=t},propHooks:{tabIndex:{get:function(n){var e=ln.find.attr(n,"tabindex");return e?parseInt(e,10):it.test(n.nodeName)||pt.test(n.nodeName)&&n.href?0:-1}}},propFix:{for:"htmlFor",class:"className"}}),rn.optSelected||(ln.propHooks.selected={get:function(n){var e=n.parentNode;return e&&e.parentNode&&e.parentNode.selectedIndex,null},set:function(n){var e=n.parentNode;e&&(e.selectedIndex,e.parentNode&&e.parentNode.selectedIndex)}}),ln.each(["tabIndex","readOnly","maxLength","cellSpacing","cellPadding","rowSpan","colSpan","useMap","frameBorder","contentEditable"],function(){ln.propFix[this.toLowerCase()]=this}),ln.fn.extend({addClass:function(d){var e,t,n,r,i,o,a,s=0;if(dn(d))return this.each(function(e){ln(this).addClass(d.call(this,e,vt(this)))});if((e=yt(d)).length)for(;t=this[s++];)if(r=vt(t),n=1===t.nodeType&&" "+dt(r)+" "){for(o=0;i=e[o++];)0>n.indexOf(" "+i+" ")&&(n+=i+" ");r!==(a=dt(n))&&t.setAttribute("class",a)}return this},removeClass:function(d){var e,t,n,r,i,o,a,s=0;if(dn(d))return this.each(function(e){ln(this).removeClass(d.call(this,e,vt(this)))});if(!arguments.length)return this.attr("class","");if((e=yt(d)).length)for(;t=this[s++];)if(r=vt(t),n=1===t.nodeType&&" "+dt(r)+" "){for(o=0;i=e[o++];)for(;-1<n.indexOf(" "+i+" ");)n=n.replace(" "+i+" "," ");r!==(a=dt(n))&&t.setAttribute("class",a)}return this},toggleClass:function(s,a){var d=typeof s,n="string"==d||Array.isArray(s);return"boolean"==typeof a&&n?a?this.addClass(s):this.removeClass(s):dn(s)?this.each(function(e){ln(this).toggleClass(s.call(this,e,vt(this),a),a)}):this.each(function(){var e,t,i,o;if(n)for(t=0,i=ln(this),o=yt(s);e=o[t++];)i.hasClass(e)?i.removeClass(e):i.addClass(e);else void 0!==s&&"boolean"!=d||((e=vt(this))&&U.set(this,"__className__",e),this.setAttribute&&this.setAttribute("class",e||!1===s?"":U.get(this,"__className__")||""))})},hasClass:function(a){var e,t,n=0;for(e=" "+a+" ";t=this[n++];)if(1===t.nodeType&&-1<(" "+dt(vt(t))+" ").indexOf(e))return!0;return!1}});var ht=/\r/g;ln.fn.extend({val:function(a){var e,t,o,n=this[0];return arguments.length?(o=dn(a),this.each(function(t){var n;1===this.nodeType&&(null==(n=o?a.call(this,t,ln(this).val()):a)?n="":"number"==typeof n?n+="":Array.isArray(n)&&(n=ln.map(n,function(t){return null==t?"":t+""})),(e=ln.valHooks[this.type]||ln.valHooks[this.nodeName.toLowerCase()])&&"set"in e&&void 0!==e.set(this,n,"value")||(this.value=n))})):n?(e=ln.valHooks[n.type]||ln.valHooks[n.nodeName.toLowerCase()])&&"get"in e&&void 0!==(t=e.get(n,"value"))?t:"string"==typeof(t=n.value)?t.replace(ht,""):null==t?"":t:void 0}}),ln.extend({valHooks:{option:{get:function(n){var e=ln.find.attr(n,"value");return null==e?dt(ln.text(n)):e}},select:{get:function(d){var e,t,n,r=d.options,i=d.selectedIndex,o="select-one"===d.type,a=o?null:[],s=o?i+1:r.length;for(n=0>i?s:o?i:0;n<s;n++)if(((t=r[n]).selected||n===i)&&!t.disabled&&(!t.parentNode.disabled||!S(t.parentNode,"optgroup"))){if(e=ln(t).val(),o)return e;a.push(e)}return a},set:function(s,e){for(var t,n,r=s.options,i=ln.makeArray(e),o=r.length;o--;)((n=r[o]).selected=-1<ln.inArray(ln.valHooks.option.get(n),i))&&(t=!0);return t||(s.selectedIndex=-1),i}}}}),ln.each(["radio","checkbox"],function(){ln.valHooks[this]={set:function(n,e){if(Array.isArray(e))return n.checked=-1<ln.inArray(ln(n).val(),e)}},rn.checkOn||(ln.valHooks[this].get=function(t){return null===t.getAttribute("value")?"on":t.value})}),rn.focusin="onfocusin"in Zt;var gt=/^(?:focusinfocus|focusoutblur)$/,mt=function(t){t.stopPropagation()};ln.extend(ln.event,{trigger:function(r,p,t,n){var b,o,a,s,u,l,c,f,d=[t||y],h=sn.call(r,"type")?r.type:r,g=sn.call(r,"namespace")?r.namespace.split("."):[];if(o=f=a=t=t||y,3!==t.nodeType&&8!==t.nodeType&&!gt.test(h+ln.event.triggered)&&(-1<h.indexOf(".")&&(g=h.split("."),h=g.shift(),g.sort()),u=0>h.indexOf(":")&&"on"+h,(r=r[ln.expando]?r:new ln.Event(h,"object"==typeof r&&r)).isTrigger=n?2:3,r.namespace=g.join("."),r.rnamespace=r.namespace?new RegExp("(^|\\.)"+g.join("\\.(?:.*\\.|)")+"(\\.|$)"):null,r.result=void 0,r.target||(r.target=t),p=null==p?[r]:ln.makeArray(p,[r]),c=ln.event.special[h]||{},n||!c.trigger||!1!==c.trigger.apply(t,p))){if(!n&&!c.noBubble&&!v(t)){for(s=c.delegateType||h,gt.test(s+h)||(o=o.parentNode);o;o=o.parentNode)d.push(o),a=o;a===(t.ownerDocument||y)&&d.push(a.defaultView||a.parentWindow||Zt)}for(b=0;(o=d[b++])&&!r.isPropagationStopped();)f=o,r.type=1<b?s:c.bindType||h,(l=(U.get(o,"events")||Object.create(null))[r.type]&&U.get(o,"handle"))&&l.apply(o,p),(l=u&&o[u])&&l.apply&&$(o)&&(r.result=l.apply(o,p),!1===r.result&&r.preventDefault());return r.type=h,n||r.isDefaultPrevented()||c._default&&!1!==c._default.apply(d.pop(),p)||!$(t)||u&&dn(t[h])&&!v(t)&&((a=t[u])&&(t[u]=null),ln.event.triggered=h,r.isPropagationStopped()&&f.addEventListener(h,mt),t[h](),r.isPropagationStopped()&&f.removeEventListener(h,mt),ln.event.triggered=void 0,a&&(t[u]=a)),r.result}},simulate:function(a,o,t){var n=ln.extend(new ln.Event,t,{type:a,isSimulated:!0});ln.event.trigger(n,null,o)}}),ln.fn.extend({trigger:function(n,e){return this.each(function(){ln.event.trigger(n,e,this)})},triggerHandler:function(a,e){var t=this[0];if(t)return ln.event.trigger(a,e,t,!0)}}),rn.focusin||ln.each({focus:"focusin",blur:"focusout"},function(a,o){var e=function(t){ln.event.simulate(o,t.target,ln.event.fix(t))};ln.event.special[o]={setup:function(){var t=this.ownerDocument||this.document||this,n=U.access(t,o);n||t.addEventListener(a,e,!0),U.access(t,o,(n||0)+1)},teardown:function(){var t=this.ownerDocument||this.document||this,n=U.access(t,o)-1;n?U.access(t,o,n):(t.removeEventListener(a,e,!0),U.remove(t,o))}}});var xt=Zt.location,Tt={guid:Date.now()},Ct=/\?/;ln.parseXML=function(a){var o,t;if(!a||"string"!=typeof a)return null;try{o=new Zt.DOMParser().parseFromString(a,"text/xml")}catch(t){}return t=o&&o.getElementsByTagName("parsererror")[0],o&&!t||ln.error("Invalid XML: "+(t?ln.map(t.childNodes,function(t){return t.textContent}).join("\n"):a)),o};var wt=/\[\]$/,St=/\r?\n/g,Et=/^(?:submit|button|image|reset|file)$/i,kt=/^(?:input|select|textarea|keygen)/i;ln.param=function(a,e){var t,o=[],n=function(a,e){var t=dn(e)?e():e;o[o.length]=encodeURIComponent(a)+"="+encodeURIComponent(null==t?"":t)};if(null==a)return"";if(Array.isArray(a)||a.jquery&&!ln.isPlainObject(a))ln.each(a,function(){n(this.name,this.value)});else for(t in a)bt(t,a[t],e,n);return o.join("&")},ln.fn.extend({serialize:function(){return ln.param(this.serializeArray())},serializeArray:function(){return this.map(function(){var t=ln.prop(this,"elements");return t?ln.makeArray(t):this}).filter(function(){var t=this.type;return this.name&&!ln(this).is(":disabled")&&kt.test(this.nodeName)&&!Et.test(t)&&(this.checked||!he.test(t))}).map(function(a,o){var e=ln(this).val();return null==e?null:Array.isArray(e)?ln.map(e,function(t){return{name:o.name,value:t.replace(St,"\r\n")}}):{name:o.name,value:e.replace(St,"\r\n")}}).get()}});var Nt=/%20/g,At=/#.*$/,jt=/([?&])_=[^&]*/,Lt=/^(.*?):[ \t]*([^\r\n]*)$/gm,qt=/^(?:GET|HEAD)$/,Ht=/^\/\//,Pt={},Ot={},It="*/".concat("*"),Mt=y.createElement("a");Mt.href=xt.href,ln.extend({active:0,lastModified:{},etag:{},ajaxSettings:{url:xt.href,type:"GET",isLocal:/^(?:about|app|app-storage|.+-extension|file|res|widget):$/.test(xt.protocol),global:!0,processData:!0,async:!0,contentType:"application/x-www-form-urlencoded; charset=UTF-8",accepts:{"*":It,text:"text/plain",html:"text/html",xml:"application/xml, text/xml",json:"application/json, text/javascript"},contents:{xml:/\bxml\b/,html:/\bhtml/,json:/\bjson\b/},responseFields:{xml:"responseXML",text:"responseText",json:"responseJSON"},converters:{"* text":String,"text html":!0,"text json":JSON.parse,"text xml":ln.parseXML},flatOptions:{url:!0,context:!0}},ajaxSetup:function(n,e){return e?Bt(Bt(n,ln.ajaxSettings),e):Bt(ln.ajaxSettings,n)},ajaxPrefilter:Dt(Pt),ajaxTransport:Dt(Ot),ajax:function(r,b){function E(o,r,t,a){var c,u,d,y,b,x=r;s||(s=!0,k&&Zt.clearTimeout(k),S=void 0,i=a||"",A.readyState=0<o?4:0,c=200<=o&&300>o||304===o,t&&(y=function(d,e,t){for(var n,r,i,o,a=d.contents,s=d.dataTypes;"*"===s[0];)s.shift(),void 0===n&&(n=d.mimeType||e.getResponseHeader("Content-Type"));if(n)for(r in a)if(a[r]&&a[r].test(n)){s.unshift(r);break}if(s[0]in t)i=s[0];else{for(r in t){if(!s[0]||d.converters[r+" "+s[0]]){i=r;break}o||(o=r)}i=i||o}return i?(i!==s[0]&&s.unshift(i),t[i]):void 0}(N,A,t)),!c&&-1<ln.inArray("script",N.dataTypes)&&0>ln.inArray("json",N.dataTypes)&&(N.converters["text script"]=function(){}),y=function(d,e,p,n){var r,i,o,a,s,h={},l=d.dataTypes.slice();if(l[1])for(o in d.converters)h[o.toLowerCase()]=d.converters[o];for(i=l.shift();i;)if(d.responseFields[i]&&(p[d.responseFields[i]]=e),!s&&n&&d.dataFilter&&(e=d.dataFilter(e,d.dataType)),s=i,i=l.shift())if("*"===i)i=s;else if("*"!==s&&s!==i){if(!(o=h[s+" "+i]||h["* "+i]))for(r in h)if((a=r.split(" "))[1]===i&&(o=h[s+" "+a[0]]||h["* "+a[0]])){!0===o?o=h[r]:!0!==h[r]&&(i=a[0],l.unshift(a[1]));break}if(!0!==o)if(o&&d.throws)e=o(e);else try{e=o(e)}catch(t){return{state:"parsererror",error:o?t:"No conversion from "+s+" to "+i}}}return{state:"success",data:e}}(N,y,A,c),c?(N.ifModified&&((b=A.getResponseHeader("Last-Modified"))&&(ln.lastModified[n]=b),(b=A.getResponseHeader("etag"))&&(ln.etag[n]=b)),204===o||"HEAD"===N.type?x="nocontent":304===o?x="notmodified":(x=y.state,u=y.data,c=!(d=y.error))):(d=x,!o&&x||(x="error",0>o&&(o=0))),A.status=o,A.statusText=(r||x)+"",c?g.resolveWith(p,[u,x,A]):g.rejectWith(p,[A,x,d]),A.statusCode(v),v=void 0,l&&h.trigger(c?"ajaxSuccess":"ajaxError",[A,N,c?u:d]),m.fireWith(p,[A,x]),l&&(h.trigger("ajaxComplete",[A,N]),--ln.active||ln.event.trigger("ajaxStop")))}"object"==typeof r&&(b=r,r=void 0),b=b||{};var S,n,i,o,k,t,s,l,c,u,N=ln.ajaxSetup({},b),p=N.context||N,h=N.context&&(p.nodeType||p.jquery)?ln(p):ln.event,g=ln.Deferred(),m=ln.Callbacks("once memory"),v=N.statusCode||{},d={},f={},x="canceled",A={readyState:0,getResponseHeader:function(n){var e;if(s){if(!o)for(o={};e=Lt.exec(i);)o[e[1].toLowerCase()+" "]=(o[e[1].toLowerCase()+" "]||[]).concat(e[2]);e=o[n.toLowerCase()+" "]}return null==e?null:e.join(", ")},getAllResponseHeaders:function(){return s?i:null},setRequestHeader:function(n,e){return null==s&&(n=f[n.toLowerCase()]=f[n.toLowerCase()]||n,d[n]=e),this},overrideMimeType:function(t){return null==s&&(N.mimeType=t),this},statusCode:function(n){if(n)if(s)A.always(n[A.status]);else for(var e in n)v[e]=[v[e],n[e]];return this},abort:function(n){var e=n||x;return S&&S.abort(e),E(0,e),this}};if(g.promise(A),N.url=((r||N.url||xt.href)+"").replace(Ht,xt.protocol+"//"),N.type=b.method||b.type||N.method||N.type,N.dataTypes=(N.dataType||"*").toLowerCase().match(P)||[""],null==N.crossDomain){t=y.createElement("a");try{t.href=N.url,t.href=t.href,N.crossDomain=Mt.protocol+"//"+Mt.host!=t.protocol+"//"+t.host}catch(t){N.crossDomain=!0}}if(N.data&&N.processData&&"string"!=typeof N.data&&(N.data=ln.param(N.data,N.traditional)),Ft(Pt,N,b,A),s)return A;for(c in(l=ln.event&&N.global)&&0==ln.active++&&ln.event.trigger("ajaxStart"),N.type=N.type.toUpperCase(),N.hasContent=!qt.test(N.type),n=N.url.replace(At,""),N.hasContent?N.data&&N.processData&&0===(N.contentType||"").indexOf("application/x-www-form-urlencoded")&&(N.data=N.data.replace(Nt,"+")):(u=N.url.slice(n.length),N.data&&(N.processData||"string"==typeof N.data)&&(n+=(Ct.test(n)?"&":"?")+N.data,delete N.data),!1===N.cache&&(n=n.replace(jt,"$1"),u=(Ct.test(n)?"&":"?")+"_="+Tt.guid++ +u),N.url=n+u),N.ifModified&&(ln.lastModified[n]&&A.setRequestHeader("If-Modified-Since",ln.lastModified[n]),ln.etag[n]&&A.setRequestHeader("If-None-Match",ln.etag[n])),(N.data&&N.hasContent&&!1!==N.contentType||b.contentType)&&A.setRequestHeader("Content-Type",N.contentType),A.setRequestHeader("Accept",N.dataTypes[0]&&N.accepts[N.dataTypes[0]]?N.accepts[N.dataTypes[0]]+("*"===N.dataTypes[0]?"":", "+It+"; q=0.01"):N.accepts["*"]),N.headers)A.setRequestHeader(c,N.headers[c]);if(N.beforeSend&&(!1===N.beforeSend.call(p,A,N)||s))return A.abort();if(x="abort",m.add(N.complete),A.done(N.success),A.fail(N.error),S=Ft(Ot,N,b,A)){if(A.readyState=1,l&&h.trigger("ajaxSend",[A,N]),s)return A;N.async&&0<N.timeout&&(k=Zt.setTimeout(function(){A.abort("timeout")},N.timeout));try{s=!1,S.send(d,E)}catch(t){if(s)throw t;E(-1,t)}}else E(-1,"No Transport");return A},getJSON:function(a,e,t){return ln.get(a,e,t,"json")},getScript:function(n,e){return ln.get(n,void 0,e,"script")}}),ln.each(["get","post"],function(n,a){ln[a]=function(o,s,d,l){return dn(s)&&(l=l||d,d=s,s=void 0),ln.ajax(ln.extend({url:o,type:a,dataType:l,data:s,success:d},ln.isPlainObject(o)&&o))}}),ln.ajaxPrefilter(function(n){for(var e in n.headers)"content-type"===e.toLowerCase()&&(n.contentType=n.headers[e]||"")}),ln._evalUrl=function(a,o,t){return ln.ajax({url:a,type:"GET",dataType:"script",cache:!0,async:!1,global:!1,converters:{"text script":function(){}},dataFilter:function(n){ln.globalEval(n,o,t)}})},ln.fn.extend({wrapAll:function(n){var e;return this[0]&&(dn(n)&&(n=n.call(this[0])),e=ln(n,this[0].ownerDocument).eq(0).clone(!0),this[0].parentNode&&e.insertBefore(this[0]),e.map(function(){for(var t=this;t.firstElementChild;)t=t.firstElementChild;return t}).append(this)),this},wrapInner:function(a){return dn(a)?this.each(function(e){ln(this).wrapInner(a.call(this,e))}):this.each(function(){var e=ln(this),t=e.contents();t.length?t.wrapAll(a):e.append(a)})},wrap:function(a){var e=dn(a);return this.each(function(t){ln(this).wrapAll(e?a.call(this,t):a)})},unwrap:function(t){return this.parent(t).not("body").each(function(){ln(this).replaceWith(this.childNodes)}),this}}),ln.expr.pseudos.hidden=function(t){return!ln.expr.pseudos.visible(t)},ln.expr.pseudos.visible=function(t){return!!(t.offsetWidth||t.offsetHeight||t.getClientRects().length)},ln.ajaxSettings.xhr=function(){try{return new Zt.XMLHttpRequest}catch(t){}};var Rt={0:200,1223:204},Wt=ln.ajaxSettings.xhr();rn.cors=!!Wt&&"withCredentials"in Wt,rn.ajax=Wt=!!Wt,ln.ajaxTransport(function(r){var d,t;if(rn.cors||Wt&&!r.crossDomain)return{send:function(e,n){var o,a=r.xhr();if(a.open(r.type,r.url,r.async,r.username,r.password),r.xhrFields)for(o in r.xhrFields)a[o]=r.xhrFields[o];for(o in r.mimeType&&a.overrideMimeType&&a.overrideMimeType(r.mimeType),r.crossDomain||e["X-Requested-With"]||(e["X-Requested-With"]="XMLHttpRequest"),e)a.setRequestHeader(o,e[o]);d=function(o){return function(){d&&(d=t=a.onload=a.onerror=a.onabort=a.ontimeout=a.onreadystatechange=null,"abort"===o?a.abort():"error"===o?"number"==typeof a.status?n(a.status,a.statusText):n(0,"error"):n(Rt[a.status]||a.status,a.statusText,"text"!==(a.responseType||"text")||"string"!=typeof a.responseText?{binary:a.response}:{text:a.responseText},a.getAllResponseHeaders()))}},a.onload=d(),t=a.onerror=a.ontimeout=d("error"),void 0===a.onabort?a.onreadystatechange=function(){4===a.readyState&&Zt.setTimeout(function(){d&&t()})}:a.onabort=t,d=d("abort");try{a.send(r.hasContent&&r.data||null)}catch(t){if(d)throw t}},abort:function(){d&&d()}}}),ln.ajaxPrefilter(function(t){t.crossDomain&&(t.contents.script=!1)}),ln.ajaxSetup({accepts:{script:"text/javascript, application/javascript, application/ecmascript, application/x-ecmascript"},contents:{script:/\b(?:java|ecma)script\b/},converters:{"text script":function(t){return ln.globalEval(t),t}}}),ln.ajaxPrefilter("script",function(t){void 0===t.cache&&(t.cache=!1),t.crossDomain&&(t.type="GET")}),ln.ajaxTransport("script",function(a){var o,t;if(a.crossDomain||a.scriptAttrs)return{send:function(e,n){o=ln("<script>").attr(a.scriptAttrs||{}).prop({charset:a.scriptCharset,src:a.url}).on("load error",t=function(a){o.remove(),t=null,a&&n("error"===a.type?404:200,a.type)}),y.head.appendChild(o[0])},abort:function(){t&&t()}}});var zt,Xt=[],Vt=/(=)\?(?=&|$)|\?\?/;ln.ajaxSetup({jsonp:"callback",jsonpCallback:function(){var t=Xt.pop()||ln.expando+"_"+Tt.guid++;return this[t]=!0,t}}),ln.ajaxPrefilter("json jsonp",function(r,e,t){var n,i,o,a=!1!==r.jsonp&&(Vt.test(r.url)?"url":"string"==typeof r.data&&0===(r.contentType||"").indexOf("application/x-www-form-urlencoded")&&Vt.test(r.data)&&"data");if(a||"jsonp"===r.dataTypes[0])return n=r.jsonpCallback=dn(r.jsonpCallback)?r.jsonpCallback():r.jsonpCallback,a?r[a]=r[a].replace(Vt,"$1"+n):!1!==r.jsonp&&(r.url+=(Ct.test(r.url)?"&":"?")+r.jsonp+"="+n),r.converters["script json"]=function(){return o||ln.error(n+" was not called"),o[0]},r.dataTypes[0]="json",i=Zt[n],Zt[n]=function(){o=arguments},t.always(function(){void 0===i?ln(Zt).removeProp(n):Zt[n]=i,r[n]&&(r.jsonpCallback=e.jsonpCallback,Xt.push(n)),o&&dn(i)&&i(o[0]),o=i=void 0}),"script"}),rn.createHTMLDocument=((zt=y.implementation.createHTMLDocument("").body).innerHTML="<form></form><form></form>",2===zt.childNodes.length),ln.parseHTML=function(a,s,d){return"string"==typeof a?("boolean"==typeof s&&(d=s,s=!1),s||(rn.createHTMLDocument?((l=(s=y.implementation.createHTMLDocument("")).createElement("base")).href=y.location.href,s.head.appendChild(l)):s=y),i=!d&&[],(r=N.exec(a))?[s.createElement(r[1])]:(r=xe([a],s,i),i&&i.length&&ln(i).remove(),ln.merge([],r.childNodes))):[];var l,r,i},ln.fn.load=function(d,l,p){var n,r,i,o=this,a=d.indexOf(" ");return-1<a&&(n=dt(d.slice(a)),d=d.slice(0,a)),dn(l)?(p=l,l=void 0):l&&"object"==typeof l&&(r="POST"),0<o.length&&ln.ajax({url:d,type:r||"GET",dataType:"html",data:l}).done(function(t){i=arguments,o.html(n?ln("<div>").append(ln.parseHTML(t)).find(n):t)}).always(p&&function(n,e){o.each(function(){p.apply(this,i||[n.responseText,e,n])})}),this},ln.expr.pseudos.animated=function(n){return ln.grep(ln.timers,function(e){return n===e.elem}).length},ln.offset={setOffset:function(d,e,t){var n,r,i,o,a,s,p=ln.css(d,"position"),l=ln(d),c={};"static"===p&&(d.style.position="relative"),a=l.offset(),i=ln.css(d,"top"),s=ln.css(d,"left"),("absolute"===p||"fixed"===p)&&-1<(i+s).indexOf("auto")?(o=(n=l.position()).top,r=n.left):(o=parseFloat(i)||0,r=parseFloat(s)||0),dn(e)&&(e=e.call(d,t,ln.extend({},a))),null!=e.top&&(c.top=e.top-a.top+o),null!=e.left&&(c.left=e.left-a.left+r),"using"in e?e.using.call(d,c):l.css(c)}},ln.fn.extend({offset:function(a){if(arguments.length)return void 0===a?this:this.each(function(e){ln.offset.setOffset(this,a,e)});var e,t,n=this[0];return n?n.getClientRects().length?(e=n.getBoundingClientRect(),t=n.ownerDocument.defaultView,{top:e.top+t.pageYOffset,left:e.left+t.pageXOffset}):{top:0,left:0}:void 0},position:function(){if(this[0]){var a,e,t,n=this[0],o={top:0,left:0};if("fixed"===ln.css(n,"position"))e=n.getBoundingClientRect();else{for(e=this.offset(),t=n.ownerDocument,a=n.offsetParent||t.documentElement;a&&(a===t.body||a===t.documentElement)&&"static"===ln.css(a,"position");)a=a.parentNode;a&&a!==n&&1===a.nodeType&&((o=ln(a).offset()).top+=ln.css(a,"borderTopWidth",!0),o.left+=ln.css(a,"borderLeftWidth",!0))}return{top:e.top-o.top-ln.css(n,"marginTop",!0),left:e.left-o.left-ln.css(n,"marginLeft",!0)}}},offsetParent:function(){return this.map(function(){for(var t=this.offsetParent;t&&"static"===ln.css(t,"position");)t=t.offsetParent;return t||oe})}}),ln.each({scrollLeft:"pageXOffset",scrollTop:"pageYOffset"},function(a,s){var t="pageYOffset"===s;ln.fn[a]=function(e){return B(this,function(n,e,a){var i;return(v(n)?i=n:9===n.nodeType&&(i=n.defaultView),void 0===a)?i?i[s]:n[e]:void(i?i.scrollTo(t?i.pageXOffset:a,t?a:i.pageYOffset):n[e]=a)},a,e,arguments.length)}}),ln.each(["top","left"],function(n,a){ln.cssHooks[a]=ze(rn.pixelPosition,function(t,e){if(e)return e=_e(t,a),De.test(e)?ln(t).position()[a]+"px":e})}),ln.each({Height:"height",Width:"width"},function(a,e){ln.each({padding:"inner"+a,content:e,"":"outer"+a},function(t,d){ln.fn[d]=function(n,r){var o=arguments.length&&(t||"boolean"!=typeof n),l=t||(!0===n||!0===r?"margin":"border");return B(this,function(e,t,n){var s;return v(e)?0===d.indexOf("outer")?e["inner"+a]:e.document.documentElement["client"+a]:9===e.nodeType?(s=e.documentElement,tn(e.body["scroll"+a],s["scroll"+a],e.body["offset"+a],s["offset"+a],s["client"+a])):void 0===n?ln.css(e,t,l):ln.style(e,t,n,l)},e,o?n:void 0,o)}})}),ln.each(["ajaxStart","ajaxStop","ajaxComplete","ajaxError","ajaxSuccess","ajaxSend"],function(n,a){ln.fn[a]=function(t){return this.on(a,t)}}),ln.fn.extend({bind:function(a,e,t){return this.on(a,null,e,t)},unbind:function(n,e){return this.off(n,null,e)},delegate:function(a,e,t,n){return this.on(e,a,t,n)},undelegate:function(a,e,t){return 1===arguments.length?this.off(a,"**"):this.off(e,a||"**",t)},hover:function(n,e){return this.mouseenter(n).mouseleave(e||n)}}),ln.each(["blur","focus","focusin","focusout","resize","scroll","click","dblclick","mousedown","mouseup","mousemove","mouseover","mouseout","mouseenter","mouseleave","change","select","submit","keydown","keypress","keyup","contextmenu"],function(n,a){ln.fn[a]=function(t,e){return 0<arguments.length?this.on(a,null,t,e):this.trigger(a)}});var Gt=/^[\s\uFEFF\xA0]+|[\s\uFEFF\xA0]+$/g;ln.proxy=function(a,e){var o,n,s;if("string"==typeof e&&(o=a[e],e=a,a=o),dn(a))return n=an.call(arguments,2),s=function(){return a.apply(e||this,n.concat(an.call(arguments)))},s.guid=a.guid=a.guid||ln.guid++,s},ln.holdReady=function(t){t?ln.readyWait++:ln.ready(!0)},ln.isArray=Array.isArray,ln.parseJSON=JSON.parse,ln.nodeName=S,ln.isFunction=dn,ln.isWindow=v,ln.camelCase=z,ln.type=w,ln.now=Date.now,ln.isNumeric=function(n){var e=ln.type(n);return("number"===e||"string"===e)&&!isNaN(n-parseFloat(n))},ln.trim=function(t){return null==t?"":(t+"").replace(Gt,"")},void 0===(t=function(){return ln}.apply(e,[]))||(Kt.exports=t);var Yt=Zt.jQuery,Qt=Zt.$;return ln.noConflict=function(t){return Zt.$===ln&&(Zt.$=Qt),t&&Zt.jQuery===ln&&(Zt.jQuery=Yt),ln},void 0===n&&(Zt.jQuery=Zt.$=ln),ln})}},e={};(()=>{"use strict";function N(t){return"string"==typeof t?document.getElementById(t):t}function A(e){return!!(e=N(e))&&"none"===getComputedStyle(e).display}function e(t){return!A(t)}function t(t){return!!t}function i(e){return /^\s*$/.test(N(e).innerHTML)}function n(n){var e=n.style;e.height=e.maxHeight=e.minHeight="auto",e.display="none"}function a(n){var e=n.style;e.height=e.maxHeight=e.minHeight="auto",e.display="none",[].forEach.call(n.children,a)}function o(t){t.style.height="1px",t.style["min-height"]="1px",t.style["max-height"]="1px",[].forEach.call(t.children,o)}function s(n){var e=n.style;e.height=e.maxHeight=e.minHeight="auto",e.removeProperty("display")}function r(a,e){var t;return function(){return a&&(t=a.call(e||this,arguments),a=null),t}}function l(n){var e=document.createElement("script");e.src=n,document.body.appendChild(e)}function c(n,a){return n.push=function(t){return a(),delete this.push,this.push(t)},n}function j(){return"undefined"!=typeof googletag&&!!googletag.apiReady}function v(){var t;j()||(window.googletag={cmd:(t=g,c([],t))})}function d(a){var e=a.split("_")[0],t=x.ids[e],o=x.slots[t];return"function"==typeof o&&(o=o(e)),{path:"/248424177/"+m+"/"+t+"/"+f,sizes:o,zone:t}}function y(l){try{Array.isArray(clc.dfp.slotsRenderedEvents)||(clc.dfp.slotsRenderedEvents=[]),clc.dfp.slotsRenderedEvents.push(l);var e=l.slot.getSlotElementId(),t=[];e||t.push("id=0");var p=document.getElementById(e);if(e&&!p?t.push("el=0"):p.hasAttribute("data-clc-stalled")&&t.push("st=1"),0!==t.length)return void b(t.join("&"));var u=d(e),i=(u.path,u.sizes,u.zone);if(clc.collapse&&clc.collapse[i]&&l.isEmpty)return p.id,a(p),void p.setAttribute("data-clc-ready","true");p.id,l.lineItemId;var h=(T.cpa_liid&&0<T.cpa_liid.length||T.cpa_cid&&0<T.cpa_cid.length)&&(T.cpa_liid&&-1!==T.cpa_liid.indexOf(l.lineItemId)||T.cpa_cid&&-1!==T.cpa_cid.indexOf(l.creativeId));if(h){o(p);var c=p.parentElement;h&&c.classList.contains("js-zone-container")&&c.querySelectorAll(".js-report-ad-button-container")[0].remove()}else if(l.lineItemId||l.creativeId||!l.isEmpty){if(p.setAttribute("data-clc-prefilled","true"),(c=p.parentElement).classList.contains("js-zone-container")){switch(n(c),p.id,c.querySelectorAll(".js-report-ad-button-container")[0].style.height="24px",e){case"dfp-tlb":0===T.tlb_position?c.classList.add("mb8"):c.classList.add("mt16");break;case"dfp-tag":c.classList.add("mb8");break;case"dfp-mlb":case"dfp-smlb":case"dfp-bmlb":c.classList.add("my8");break;case"dfp-isb":c.classList.add("mt24");break;case"dfp-m-aq":c.classList.add("my12"),c.classList.add("mx-auto");}s(c),s(p)}else s(p);"dfp-msb"==e&&a(document.getElementById("hireme"))}p.setAttribute("data-clc-ready","true")}catch(t){var g=document.querySelector("#dfp-tsb, #dfp-isb, #clc-tsb");g&&g.setAttribute("data-clc-ready","true"),b("e=1")}}function u(l,e){"dfp-isb"===l&&e.pubads().setTargeting("Sidebar",["Inline"]),"dfp-tsb"===l&&e.pubads().setTargeting("Sidebar",["Right"]);var t=d(l),n=t.path,r=t.sizes;t.zone,JSON.stringify(r);var i=e.defineSlot(n,r,l);i.addService(e.pubads());var o=l.split("_");if("clc-cpa"==o[0]&&o[1]){var a=o[1];i.setTargeting("talent-company-id",a)}}window.clc=window.clc||{};var T=function(a,e){for(var t in e)a[t]=e[t];return a}({"lib":"https://cdn.sstatic.net/clc/clc.min.js?v=57e591b1e46b","style":"https://cdn.sstatic.net/clc/styles/clc.min.css?v=3054624618f9","u":"https://clc.stackoverflow.com/markup.js","wa":true,"kt":2000,"tto":true,"h":"clc.stackoverflow.com","allowed":"^(((talent\\.)?stackoverflow)|(blog\\.codinghorror)|(serverfault|askubuntu)|([^\\.]+\\.stackexchange))\\.com$","wv":true,"al":false,"abd":true,"cpa_liid":[5882654614],"cpa_cid":[138377597667],"dp":false},clc.options||{}),p=r(function(){l(T.lib)});window.clc=window.clc||{},clc.cmd=clc.cmd||[];var h=clc.cmd;Array.isArray(clc.cmd)&&(0<clc.cmd.length?p():c(clc.cmd,p));var g=r(function(){T.targeting_consent||void 0===T.targeting_consent?l("https://securepubads.g.doubleclick.net/tag/js/gpt.js"):l("https://pagead2.googlesyndication.com/tag/js/gpt.js")}),f=/^\/tags\//.test(location.pathname)||/^\/questions\/tagged\//.test(location.pathname)?"tag-pages":/^\/$/.test(location.pathname)||/^\/home/.test(location.pathname)?"home-page":"question-pages",m=location.hostname,x={slots:{lb:[[728,90]],mlb:[[728,90]],smlb:[[728,90]],bmlb:[[728,90]],sb:function(t){return"dfp-tsb"===t?[[300,250],[300,600]]:[[300,250]]},"tag-sponsorship":[[730,135]],"mobile-below-question":[[320,50],[300,250]],msb:[[300,250],[300,600]],"talent-conversion-tracking":[[1,1]]},ids:{"dfp-tlb":"lb","dfp-mlb":"mlb","dfp-smlb":"smlb","dfp-bmlb":"bmlb","dfp-tsb":"sb","dfp-isb":"sb","dfp-tag":"tag-sponsorship","dfp-msb":"msb","dfp-m-aq":"mobile-below-question","clc-tlb":"lb","clc-mlb":"mlb","clc-tsb":"sb","clc-cpa":"talent-conversion-tracking"}},b=function(t){new Image().src="https://"+T.h+"/stalled.gif?"+t};window.onmessage=function(a){var e="click-url:";if(a.data&&("string"==typeof a.data||a.data instanceof String)&&0===a.data.indexOf(e)){var t=a.data.slice(e.length);a.data,document.getElementById("hireme").setAttribute("data-cpa-gam-click-url",t)}},k(291),window.clc=window.clc||{},clc.options=T,clc.cmd=h,clc.dfp={load:function o(s){void 0===s&&(s=Object.keys(x.ids).filter(function(t){return"clc-cpa"!=t}));var r=0===T.tlb_position?["dfp-mlb","dfp-smlb"]:["dfp-mlb","dfp-smlb","dfp-tlb"];if(!j())return v(),void googletag.cmd.push(function(){return o(s)});var l=function(o){var n=o.map(N).filter(t);return{eligible:n.filter(i).filter(e),ineligible:n.filter(A)}}(s),p=l.eligible,c=l.ineligible;if(p.forEach(function(t){n(t)}),c.forEach(a),0!==p.length){var d;T.abd&&((d=document.createElement("div")).className="adsbox",d.id="clc-abd",d.style.position="absolute",d.style.pointerEvents="none",d.innerHTML="&nbsp;",document.body.appendChild(d));var h=googletag.pubads().getSlots().filter(function(t){return 0<=s.indexOf(t.getSlotElementId())});googletag.destroySlots(h),T.sf&&(googletag.pubads().setForceSafeFrame(!0),googletag.pubads().setSafeFrameConfig({allowOverlayExpansion:!0,allowPushExpansion:!0,sandbox:!0})),void 0!==T.targeting_consent&&(T.targeting_consent,googletag.pubads().setRequestNonPersonalizedAds(T.targeting_consent?0:1),T.targeting_consent||googletag.pubads().setPrivacySettings({limitedAds:!0})),T.ll||googletag.pubads().enableSingleRequest(),window.clc=window.clc||{},clc.sreEvent||(googletag.pubads().addEventListener("slotRenderEnded",y),clc.sreEvent=!0),function(a){var e=window.clc&&clc.dfp&&clc.dfp.targeting||{};"SystemDefault"===e.ProductVariant&&(window.matchMedia&&window.matchMedia("(prefers-color-scheme: dark)").matches?e.ProductVariant="Dark":e.ProductVariant="Light"),Object.keys(e).forEach(function(t){e[t],a.pubads().setTargeting(t,e[t])})}(googletag);var g=p.filter(function(t){return!T.ll||0>r.indexOf(t.id)}),f=p.filter(function(t){return!!T.ll&&0<=r.indexOf(t.id)});g.forEach(function(t){t.id,u(t.id,googletag),t.setAttribute("data-dfp-zone","true")}),googletag.enableServices(),g.forEach(function(t){t.id,googletag.cmd.push(function(){googletag.display(t.id)})}),T.ll&&(googletag.pubads().enableLazyLoad({fetchMarginPercent:0,renderMarginPercent:0}),f.forEach(function(t){t.id,u(t.id,googletag),t.setAttribute("data-clc-prefilled","true")}),f.forEach(function(t){t.id,googletag.cmd.push(function(){googletag.display(t.id)})}))}}},T.al&&h.push(function(){return clc.load()}),v()})()})();</script><script>
    var clc = clc || {};
    clc.collapse = { sb: !0, 'tag-sponsorship': !0, lb: !0, mlb: !0, smlb: !0, bmlb: !0, 'mobile-below-question': !0 };
    clc.options = clc.options || {};
    clc.options.sf = !0;
    clc.options.hb = !1;
    clc.options.ll = !0;
    clc.options.tlb_position = 0;
    clc.options.targeting_consent = !1;
    clc.options.performance_consent = !1;
        clc.cmd = clc.cmd || [];
        clc.cmd.push(function () { window.clc_request='A_gFzVQZaNoIAAAAAMQZWgQCAAAAAgAAAAAADwAAAHxweXRob258ZGphbmdvfABi34ansiO3pQjy'; clc.load(); });
        clc.dfp = clc.dfp || {};
        clc.dfp.targeting = {Registered:['false'],'so-tag':['python','django'],'tag-reportable':['python','django'],'tag-non-reportable':['python','django'],NumberOfAnswers:['1']};

        if (window.location.hash.indexOf('ads:cat=cp') >= 0)
        {
            clc.dfp.targeting.CompanyPageAd = '1';
        }

        clc.dfp.targeting.TargetingConsent = ['False_Passive'];

        const urlParams = new URLSearchParams(window.location.search);
        if (urlParams.has('dfptestads')) {
            const dfptestads = urlParams.get('dfptestads');
            clc.dfp.targeting.DfpTestAds = dfptestads;
        }

        var googletag = googletag || {};
        googletag.cmd = googletag.cmd || [];
        googletag.cmd.push(function () { clc.dfp.load(); });
        StackExchange.ready(function () { googletag.cmd.push(function () { StackExchange.ads.init(googletag, '/ads/report-ad', 'Report this ad') }) });
</script><script src="https://cdn.sstatic.net/clc/clc.min.js?v=57e591b1e46b"></script><script src="https://pagead2.googlesyndication.com/tag/js/gpt.js"></script>

            <footer id="footer" class="site-footer js-footer" role="contentinfo">
        <div class="site-footer--container">
                <div class="site-footer--logo">

                    <a href="https://stackoverflow.com"><svg aria-hidden="true" class="native svg-icon iconLogoGlyphMd" width="32" height="37" viewBox="0 0 32 37"><path d="M26 33v-9h4v13H0V24h4v9h22Z" fill="#BCBBBB"></path><path d="m21.5 0-2.7 2 9.9 13.3 2.7-2L21.5 0ZM26 18.4 13.3 7.8l2.1-2.5 12.7 10.6-2.1 2.5ZM9.1 15.2l15 7 1.4-3-15-7-1.4 3Zm14 10.79.68-2.95-16.1-3.35L7 23l16.1 2.99ZM23 30H7v-3h16v3Z" fill="#F48024"></path></svg></a>
                </div>
            <nav class="site-footer--nav">
                    <div class="site-footer--col">
                        <h5 class="-title"><a href="https://stackoverflow.com" class="js-gps-track" data-gps-track="footer.click({ location: 2, link: 15})">Stack Overflow</a></h5>
                        <ul class="-list js-primary-footer-links">
                            <li><a href="/questions" class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 16})">Questions</a></li>
                                <li><a href="/help" class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 3 })">Help</a></li>
                        </ul>
                    </div>
                    <div class="site-footer--col">
                        <h5 class="-title"><a href="https://stackoverflow.com/?products" class="js-gps-track" data-gps-track="footer.click({ location: 2, link: 19 })">Products</a></h5>
                        <ul class="-list">
                            <li><a href="https://stackoverflow.co/teams" class="js-gps-track -link" data-ga="[&quot;teams traffic&quot;,&quot;footer - site nav&quot;,&quot;stackoverflow.com/teams&quot;,null,{&quot;dimension4&quot;:&quot;teams&quot;}]" data-gps-track="footer.click({ location: 2, link: 29 })">Teams</a></li>
                            <li><a href="https://stackoverflow.co/advertising" class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 21 })">Advertising</a></li>
                            <li><a href="https://stackoverflow.co/collectives" class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 40 })">Collectives</a></li>
                            <li><a href="https://stackoverflow.co/talent" class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 20 })">Talent</a></li>
                        </ul>
                    </div>
                <div class="site-footer--col">
                    <h5 class="-title"><a class="js-gps-track" data-gps-track="footer.click({ location: 2, link: 1 })" href="https://stackoverflow.co/">Company</a></h5>
                    <ul class="-list">
                            <li><a class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 1 })" href="https://stackoverflow.co/">About</a></li>
                        <li><a class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 27 })" href="https://stackoverflow.co/company/press">Press</a></li>
                            <li><a class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 9 })" href="https://stackoverflow.co/company/work-here">Work Here</a></li>
                        <li><a class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 7 })" href="https://stackoverflow.com/legal">Legal</a></li>
                        <li><a class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 8 })" href="https://stackoverflow.com/legal/privacy-policy">Privacy Policy</a></li>
                        <li><a class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 37 })" href="https://stackoverflow.com/legal/terms-of-service">Terms of Service</a></li>
                            <li><a class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 13 })" href="https://stackoverflow.co/company/contact">Contact Us</a></li>
                            <li class="" id="consent-footer-link"><a class="js-gps-track -link js-cookie-settings" data-gps-track="footer.click({ location: 2, link: 38 })" href="#" data-consent-popup-loader="footer">Cookie Settings</a></li>
                        <li><a class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 39 })" href="https://stackoverflow.com/legal/cookie-policy">Cookie Policy</a></li>
                    </ul>
                </div>
                <div class="site-footer--col site-footer--categories-nav">
                    <div>
                        <h5 class="-title"><a href="https://stackexchange.com" data-gps-track="footer.click({ location: 2, link: 30 })">Stack Exchange Network</a></h5>
                        <ul class="-list">
                            <li>
                                <a href="https://stackexchange.com/sites#technology" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 24 })">
                                    Technology
                                </a>
                            </li>
                            <li>
                                <a href="https://stackexchange.com/sites#culturerecreation" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 24 })">
                                    Culture &amp; recreation
                                </a>
                            </li>
                            <li>
                                <a href="https://stackexchange.com/sites#lifearts" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 24 })">
                                    Life &amp; arts
                                </a>
                            </li>
                            <li>
                                <a href="https://stackexchange.com/sites#science" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 24 })">
                                    Science
                                </a>
                            </li>
                            <li>
                                <a href="https://stackexchange.com/sites#professional" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 24 })">
                                    Professional
                                </a>
                            </li>
                            <li>
                                <a href="https://stackexchange.com/sites#business" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 24 })">
                                    Business
                                </a>
                            </li>

                            <li class="mt16 md:mt0">
                                <a href="https://api.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 24 })">
                                    API
                                </a>
                            </li>

                            <li>
                                <a href="https://data.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 24 })">
                                    Data
                                </a>
                            </li>
                        </ul>
                    </div>
                </div>
            </nav>
            <div class="site-footer--copyright fs-fine md:mt24">
                <ul class="-list -social md:mb8">
                    <li><a class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link:4 })" href="https://stackoverflow.blog?blb=1">Blog</a></li>
                    <li><a href="https://www.facebook.com/officialstackoverflow/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 31 })">Facebook</a></li>
                    <li><a href="https://twitter.com/stackoverflow" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 32 })">Twitter</a></li>
                    <li><a href="https://linkedin.com/company/stack-overflow" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 33 })">LinkedIn</a></li>
                    <li><a href="https://www.instagram.com/thestackoverflow" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 36 })">Instagram</a></li>
                </ul>

                <p class="md:mb0">
Site design / logo © 2022 Stack Exchange Inc; user contributions licensed under <a href="https://stackoverflow.com/help/licensing">cc by-sa</a>.                    <span id="svnrev">rev&nbsp;2022.7.15.42606</span>
                </p>
            </div>
        </div>

    </footer>


        <script>
    </script>


                <div class="ff-sans ps-fixed z-nav-fixed ws4 sm:w-auto p32 sm:p16 bg-black-750 fc-white bar-lg b16 l16 r16 js-consent-banner" style="display: none;">
                    <svg aria-hidden="true" class="mln4 mb24 sm:d-none svg-spot spotCookieLg" style="color: var(--theme-button-filled-background-color)" width="96" height="96" viewBox="0 0 96 96">
                        <path d="M35 45.5a7.5 7.5 0 11-15 0 7.5 7.5 0 0115 0zM63.5 63a7.5 7.5 0 100-15 7.5 7.5 0 000 15zm-19 19a7.5 7.5 0 100-15 7.5 7.5 0 000 15z" opacity=".2"></path>
                        <path d="M56.99 2.53a23.1 23.1 0 0114.66 6.15h.01l.01.02c.57.55.61 1.27.5 1.74v.07a10.95 10.95 0 01-3.07 4.77 9 9 0 01-6.9 2.5 10.34 10.34 0 01-9.72-10.44v-.08a10 10 0 011.03-3.74l.01-.03.02-.02c.28-.5.82-.92 1.52-.95.63-.02 1.27-.02 1.93.01zm12.04 7.83a20.1 20.1 0 00-12.2-4.83l-.92-.03c-.23.6-.38 1.25-.43 1.94a7.34 7.34 0 006.95 7.34 6 6 0 004.64-1.7c.94-.88 1.6-1.9 1.96-2.72zm15.3 8.76a6.84 6.84 0 00-5.09-.24 7.9 7.9 0 00-3.28 2.05 1.8 1.8 0 00-.3 1.95l.02.02v.02a15.16 15.16 0 008.74 7.47c.64.23 1.32.08 1.8-.33a6.63 6.63 0 001.63-1.97l.01-.03.01-.03c1.67-3.5-.12-7.32-3.54-8.91zm-5.5 3.28c.36-.25.82-.5 1.35-.67.92-.3 1.92-.35 2.89.1 2.14 1 2.92 3.14 2.11 4.88-.12.21-.26.41-.43.6l-.26-.1a12.29 12.29 0 01-5.66-4.81zM32 24a2 2 0 11-4 0 2 2 0 014 0zm12 21a2 2 0 11-4 0 2 2 0 014 0zm36 4a2 2 0 11-4 0 2 2 0 014 0zm-7 21a2 2 0 11-4 0 2 2 0 014 0zM59 81a2 2 0 11-4 0 2 2 0 014 0zM22 63a2 2 0 11-4 0 2 2 0 014 0zm27 7a9 9 0 11-18 0 9 9 0 0118 0zm-3 0a6 6 0 10-12 0 6 6 0 0012 0zM33 41a9 9 0 11-18 0 9 9 0 0118 0zm-15 0a6 6 0 1012 0 6 6 0 00-12 0zm50 11a9 9 0 11-18 0 9 9 0 0118 0zm-3 0a6 6 0 10-12 0 6 6 0 0012 0zM44.08 4.24c.31.48.33 1.09.05 1.58a17.46 17.46 0 00-2.36 8.8c0 9.55 7.58 17.24 16.85 17.24 2.97 0 5.75-.78 8.16-2.15a1.5 1.5 0 012.1.66 12.08 12.08 0 0011 6.74 12.4 12.4 0 007.85-2.75 1.5 1.5 0 012.38.74A45.76 45.76 0 0192 48.16c0 24.77-19.67 44.9-44 44.9S4 72.93 4 48.16C4 25.23 20.84 6.28 42.64 3.58a1.5 1.5 0 011.44.66zM40.22 7C21.32 10.71 7 27.7 7 48.16c0 23.17 18.39 41.9 41 41.9s41-18.73 41-41.9c0-3.52-.42-6.93-1.22-10.2a15.5 15.5 0 01-7.9 2.15c-5.5 0-10.36-2.83-12.97-7.1a19.46 19.46 0 01-8.28 1.85c-11 0-19.86-9.1-19.86-20.24 0-2.7.52-5.26 1.45-7.62zM92 91a2 2 0 100-4 2 2 0 000 4zM7 8.5a2.5 2.5 0 11-5 0 2.5 2.5 0 015 0zM82.5 90a1.5 1.5 0 100-3 1.5 1.5 0 000 3zm9.5-7.5a1.5 1.5 0 11-3 0 1.5 1.5 0 013 0zM13.5 8a1.5 1.5 0 100-3 1.5 1.5 0 000 3zM80 14.5a1.5 1.5 0 11-3 0 1.5 1.5 0 013 0zM53.5 20a1.5 1.5 0 100-3 1.5 1.5 0 000 3z"></path>
                    </svg>
                    <p class="fs-body2 fw-bold mb4">
                        Your privacy
                    </p>
                    <p class="mb16 s-anchors s-anchors__inherit s-anchors__underlined">
                        By clicking “Accept all cookies”, you agree Stack Exchange can store cookies on your device and disclose information in accordance with our <a href="https://stackoverflow.com/legal/cookie-policy">Cookie Policy</a>.
                    </p>
                    <div class="d-flex gs8 ai-stretch fd-column sm:fd-row">
                        <button class="flex--item s-btn s-btn__primary js-accept-cookies js-consent-banner-hide">
                            Accept all cookies
                        </button>

                        <button class="flex--item s-btn s-btn__filled js-cookie-settings" data-consent-popup-loader="banner">
                            Customize settings
                        </button>
                    </div>
                </div>
    <div id="onetrust-consent-sdk" class="d-none"><div class="onetrust-pc-dark-filter ot-hide ot-fade-in"></div></div>
    <div id="onetrust-banner-sdk" data-controller="s-modal"></div>
    <div id="ot-pc-content" class="d-none"></div>

    <div class="d-none js-consent-banner-version" data-consent-banner-version="baseline"></div>




<script type="text/javascript" charset="UTF-8" data-domain-script="c3d9f1e3-55f3-4eba-b268-46cee4c6789c" async="true" src="https://cdn.cookielaw.org/scripttemplates/otSDKStub.js"></script></body></html>
'''
