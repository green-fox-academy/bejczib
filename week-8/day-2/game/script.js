'use strict';

function Game() {
    this.createCandies = document.querySelector('.create-candies');
    this.candies = document.querySelector('.candies');
    this.buyLollypop = document.querySelector('.buy-lollypops');
    this.buy10lollypops = document.querySelector('.buy-10lollypops');
    this.lollypops = document.querySelector('.lollypops');
    this.speed = document.querySelector('.speed');
    this.candiIndex = 0;
    this.lollypopIndex = 8;
    this.speedIndex = 1;


    var _this = this;

    this.buttonChecker = function() {
        if (this.candiIndex < 10) {
            this.setButtonDisable('.buy-lollypops');
        } else {
            this.setButtonEnable('.buy-lollypops');
        }
        if (this.candiIndex >= 100) {
            this.setButtonEnable('.buy-10lollypops');
        } else {
            this.setButtonDisable('.buy-10lollypops');
        }
    }

    this.createCandies.addEventListener('click', function () {
        _this.buttonChecker();
        _this.candiIndex++;
        _this.candies.innerHTML = _this.candiIndex;
    });

    this.setButtonDisable = function(_class) {
        document.querySelector(_class).setAttribute('disabled','');
    }

    this.setButtonEnable  = function(_class) {
        document.querySelector(_class).removeAttribute('disabled');
    }

    this.buyLollypop.addEventListener('click', function () {
        if (_this.candiIndex >= 10) {
            _this.lollypopIndex++;
            _this.lollypops.innerHTML = _this.lollypopIndex;
            _this.candies.innerHTML -= 10;
            _this.candiIndex -=10;
        }
        _this.buttonChecker();
    });

    setInterval(function() {
        if (_this.lollypopIndex >= 10) {
            _this.buttonChecker();
            _this.speedIndex = Math.floor(_this.lollypopIndex/10);
            _this.speed.innerHTML = _this.speedIndex;
            _this.candiIndex+= _this.speedIndex;
            _this.candies.innerHTML = _this.candiIndex;

        }
    }, 1000);

    this.buy10lollypops.addEventListener('click', function() {
        if (_this.candiIndex >= 100) {
            _this.lollypopIndex += 10;
            _this.lollypops.innerHTML = _this.lollypopIndex;
            _this.candies.innerHTML -= 100;
            _this.candiIndex -=100;
        }
        _this.buttonChecker();
    });

    this.startGame = function() {
        this.setButtonDisable('.buy-lollypops');
        this.setButtonDisable('.buy-10lollypops');
    }
}
var game = new Game();

game.startGame();




