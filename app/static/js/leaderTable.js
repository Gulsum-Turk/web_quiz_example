var properties = [
    'name',
    'wins',
    'draws',
    'losses',
    'total',
];

properties.forEach(function(val) {
    var orderClass = '';

    document.getElementById(val).addEventListener('click', function(e) {
        e.preventDefault();
        var activeLinks = document.querySelectorAll('.filter__link.filter__link--active');
        activeLinks.forEach(function(link) {
            if (link !== this) {
                link.classList.remove('filter__link--active');
            }
        }.bind(this));
        this.classList.toggle('filter__link--active');
        var allLinks = document.querySelectorAll('.filter__link');
        allLinks.forEach(function(link) {
            link.classList.remove('asc', 'desc');
        });

        if (orderClass === 'desc' || orderClass === '') {
            this.classList.add('asc');
            orderClass = 'asc';
        } else {
            this.classList.add('desc');
            orderClass = 'desc';
        }

        var parent = this.closest('.header__item');
        var index = Array.prototype.indexOf.call(document.querySelectorAll('.header__item'), parent);
        var table = document.querySelector('.table-content');
        var rows = Array.from(table.querySelectorAll('.table-row'));

        rows.sort(function(a, b) {
            var x = a.querySelectorAll('.table-data')[index].textContent;
            var y = b.querySelectorAll('.table-data')[index].textContent;

            if (this.classList.contains('filter__link--number')) {
                if (this.classList.contains('filter__link--active')) {
                    return parseInt(x) - parseInt(y);
                } else {
                    return parseInt(y) - parseInt(x);
                }
            } else {
                if (this.classList.contains('filter__link--active')) {
                    return x.localeCompare(y);
                } else {
                    return y.localeCompare(x);
                }
            }
        }.bind(this));

        rows.forEach(function(row) {
            table.appendChild(row);
        });

        return false;
    });
});
