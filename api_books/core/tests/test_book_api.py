from http import HTTPStatus

from django.shortcuts import resolve_url


def test_book_get(client, book):
    resp = client.get(resolve_url('book_list'))

    expected = [book.to_dict()]

    assert resp.status_code == HTTPStatus.OK
    assert resp.json()['result'] == expected


def test_book_get_by_id(client, books):

    book = books[1]

    resp = client.get(resolve_url('books', book.id))

    expected = book.to_dict()

    assert resp.status_code == HTTPStatus.OK
    assert resp.json() == expected


def test_book_get_by_id_not_exist(client, books):

    ID = 404
    resp = client.get(resolve_url('books', ID))

    assert resp.status_code == HTTPStatus.OK
    assert resp.json() == {'error': f'Id {ID} not found!'}
