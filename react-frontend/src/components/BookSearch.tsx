import axios from 'axios';
import { useState, BaseSyntheticEvent, useRef } from 'react';
import { BookModel } from '../models/BookModel';
import edition_placeholder from '../assets/edition_placeholder.png'
import ImageList from '@mui/material/ImageList';
import ImageListItem from '@mui/material/ImageListItem';
import ImageListItemBar from '@mui/material/ImageListItemBar';
import IconButton from '@mui/material/IconButton';
import InfoIcon from '@mui/icons-material/Info';
import "./BookSearch.css";


function BookSearch() {

    const [book, setBook] = useState("");
    const [result, setResult] = useState([]);
    const linkRef = useRef<HTMLAnchorElement>(null);

    async function getBooksByName(book: string) {
        try {
            const response = await axios.get(`http://localhost:8000/books_by_name?book=${book}`);
            return response.data;
        } catch (error) {
            console.error('Error fetching books: ', error);
            throw error;
        }
        
    }

    function handleChange(event: BaseSyntheticEvent) {
        const book = event.target.value;
        setBook(book);
    }

    function handleSubmit(event: BaseSyntheticEvent) {
        event.preventDefault();

        getBooksByName(book)
        .then((data) => {
            setResult(data);
        })
        .catch((error) => {
            console.error('Error: ', error)
        })
    }

    function openNewWindow(previewLink: string) {
        window.open(previewLink, '_blank');
    }

    return (
        <div className="container">
            <h1 className='subtitle'>Book Search</h1>
            <form onSubmit={handleSubmit} className='form'>
                <div className="form-group">
                    <input 
                        type="text" 
                        onChange={handleChange}
                        className="form-control mt-10" 
                        placeholder="Search for books" 
                        autoComplete="off" 
                    />
                </div>
                <button type="submit" className="submit-button">Search</button>
            </form>
            <ImageList sx={{ width: '100%', height: 650 }} cols={8}>
                {result.map((book: BookModel) => (
                    <ImageListItem key={book.volumeInfo.imageLinks?.thumbnail || edition_placeholder}>
                    <img
                        srcSet={`${book.volumeInfo.imageLinks?.thumbnail || edition_placeholder}?w=248&fit=crop&auto=format&dpr=2 2x`}
                        src={`${book.volumeInfo.imageLinks?.thumbnail || edition_placeholder}?w=248&fit=crop&auto=format`}
                        alt={book.volumeInfo.title}
                        loading="lazy"
                    />
                    <ImageListItemBar
                        title={book.volumeInfo.title}
                        subtitle={book.volumeInfo.authors}
                        actionIcon={
                            <a href='#' ref={linkRef} onClick={() => openNewWindow(book.volumeInfo.previewLink)}>
                                <IconButton
                                    sx={{ color: 'rgba(255, 255, 255, 0.54)' }}
                                    aria-label={`info about ${book.volumeInfo.title}`}
                                >
                                    <InfoIcon />
                                </IconButton>
                            </a>
                        }
                    />
                    </ImageListItem>
                ))}
            </ImageList>
        </div>
    )
}

export default BookSearch;